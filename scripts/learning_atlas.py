"""Learner-facing views of the preserved curriculum; no canonical ID migration."""

import json
import os
import re
from collections import defaultdict
from html import escape
from pathlib import Path
from urllib.parse import urlsplit

import yaml
from jsonschema import Draft202012Validator

if __package__:
    from .frontier_data import load_frontier, load_tracks
else:
    from frontier_data import load_frontier, load_tracks

ROOT = Path(__file__).resolve().parents[1]


def load_json(root, path):
    return json.loads((root / path).read_text(encoding="utf-8"))


def build_atlas(root=ROOT):
    design = load_json(root, "data/learning-design.json")
    schema = load_json(ROOT, "schemas/learning-design.schema.json")
    Draft202012Validator(schema).validate(design)
    modules = load_json(root, "data/obelisk/modules.json")["modules"]
    nodes = load_json(root, "data/obelisk/nodes.json")["nodes"]
    resources = load_json(root, "data/obelisk/sources.json")["sources"]
    links = load_json(root, "data/obelisk/source-links.json")["links"]
    evidence = load_json(root, "data/obelisk/content-evidence.json")["targets"]
    foundations = design["foundations"]
    memberships = {}
    for key, foundation in foundations.items():
        for branch in foundation["branches"]:
            if branch in memberships:
                raise ValueError(f"Duplicate foundation membership: {branch}")
            memberships[branch] = key
    for key, view in design["support_views"].items():
        if key in foundations:
            raise ValueError(f"Duplicate learner view: {key}")
        for branch in view["branches"]:
            if branch in memberships:
                raise ValueError(f"Duplicate support branch membership: {branch}")
            memberships[branch] = key
    subjects = {}
    for record in modules + [node for node in nodes if not node.get("module_id")]:
        identity = record["id"]
        journey = design["journeys"].get(identity, {})
        outcomes = [{**node, "kind": "outcome"} for node in nodes if node.get("module_id") == identity]
        targets = {identity, *(node["id"] for node in outcomes)}
        recommendations = [link for link in links if link["target_id"] in targets]
        subjects[identity] = {
            **record, "kind": "subject", "title": journey.get("title", record["title"]),
            "path": f"docs/learn/{journey.get('slug', identity.lower())}.md",
            "foundation": memberships[record["branch_id"]],
            "prerequisites": record.get("prerequisite_ids", []),
            "resources": sorted({link["source_id"] for link in recommendations}),
            "recommendations": recommendations,
            "outcomes": outcomes,
            "teaching": evidence.get(identity, {}).get("teaching_path"),
            "journey": journey,
        }
    if len({subject["path"] for subject in subjects.values()}) != len(subjects):
        raise ValueError("Duplicate learner route")
    resource_index = {resource["id"]: {**resource, "kind": "resource"} for resource in resources}
    for resource in resource_index.values():
        if resource.get("record_kind", "work") not in {"work", "reading-area"}:
            raise ValueError(f"Unknown source record kind: {resource['id']}")
        if resource.get("role") == "Gap/Search" and resource.get("record_kind") != "reading-area":
            raise ValueError(f"Source gap must be a reading area: {resource['id']}")
    for subject in subjects.values():
        for identity in subject["prerequisites"] + subject["journey"].get("connections", []):
            if identity not in subjects:
                raise ValueError(f"Unknown subject reference: {identity}")
        for identity in subject["resources"]:
            if identity not in resource_index:
                raise ValueError(f"Unknown resource reference: {identity}")
    for foundation in [*foundations.values(), *design["support_views"].values()]:
        if any(identity not in subjects for identity in foundation["entry"]):
            raise ValueError("Unknown foundation entry")
    technology_study = load_json(root, "data/obelisk/technology-study.json")
    Draft202012Validator(load_json(ROOT, "schemas/obelisk/technology-study.schema.json")).validate(technology_study)
    technologies = {}
    frontier = load_frontier(root)
    for record in frontier["technologies"]:
        paths = list((root / "docs/05-frontier/technologies").glob(f"{record['id']:03d}-*.md"))
        if len(paths) != 1:
            raise ValueError(f"Technology must have one detail page: {record['id']}")
        technologies[record["id"]] = {**record, "path": paths[0].relative_to(root).as_posix(), "study": []}
    for subject in subjects.values():
        subject["technologies"] = []
    seen = set()
    for connection in technology_study["connections"]:
        technology_id, subject_id = connection["technology_id"], connection["subject_id"]
        if subject_id not in subjects:
            raise ValueError(f"Unknown technology study subject: {subject_id}")
        if technology_id not in technologies:
            raise ValueError(f"Unknown technology study target: {technology_id}")
        if (technology_id, subject_id) in seen:
            raise ValueError(f"Duplicate technology study connection: {technology_id}, {subject_id}")
        seen.add((technology_id, subject_id))
        technologies[technology_id]["study"].append(connection)
        subjects[subject_id]["technologies"].append(technology_id)
    relations = []
    for subject in subjects.values():
        relations.extend({"kind": "requires", "from": subject["id"], "to": identity}
                         for identity in subject["prerequisites"])
        relations.extend({"kind": "part-of", "from": outcome["id"], "to": subject["id"]}
                         for outcome in subject["outcomes"])
        relations.extend({"kind": "related-inquiry", "from": subject["id"], "to": identity}
                         for identity in subject["journey"].get("connections", []))
    relations.extend({"kind": "reading-recommendation", "from": link["source_id"],
                      "to": link["target_id"], "role": link["role"]} for link in links)
    return {"schema_version": 1, "subjects": subjects, "resources": resource_index,
            "foundations": foundations, "relations": relations, "technologies": technologies,
            "technology_study_policy": technology_study["policy"], "support_views": design["support_views"],
            "branch_labels": design["branch_labels"], "tracks": load_tracks(root), "technology_classes": frontier["classes"]}


def relative_link(source, target):
    return os.path.relpath(target, Path(source).parent).replace("\\", "/")


def subject_link(subject, source):
    return f"[{subject['title']}]({relative_link(source, subject['path'])})"


def html_link(title, target):
    return f'<a href="{escape(target, quote=True)}">{escape(title)}</a>'


def resource_actions(resource, source):
    detail = relative_link(source, f"docs/library/{resource['id'].lower()}.md")
    actions = [html_link("Reading details", detail)]
    if resource.get("record_kind") == "reading-area":
        actions.insert(0, "Selection needed")
    elif resource.get("url"):
        actions.insert(0, html_link("Open resource", resource["url"]))
    return f'<p class="atlas-reading"><strong>{escape(resource["title"])}</strong><br>{" &middot; ".join(actions)}</p>'


def subject_preview(subject, atlas, source):
    label = "Practice available" if subject["teaching"] else "Outline"
    purpose = subject.get("exit_capability") or subject.get("mastery_test", "")
    resource_available = any(atlas["resources"][identity].get("url") and
                             atlas["resources"][identity].get("record_kind") != "reading-area"
                             for identity in subject["resources"])
    lines = [f'<li data-practice="{str(bool(subject["teaching"])).lower()}" data-resource="{str(resource_available).lower()}">',
             '<details class="atlas-preview">',
             f'<summary><strong>{escape(subject["title"])}</strong><span class="atlas-status">{label}</span></summary>',
             f'<p>{escape(purpose)}</p>']
    prerequisites = [html_link(atlas["subjects"][identity]["title"],
                    relative_link(source, atlas["subjects"][identity]["path"])) for identity in subject["prerequisites"]]
    readiness = "; ".join(prerequisites) or ("No subject prerequisite recorded." if "prerequisite_ids" in subject
                                            else "Preparation guidance is not established.")
    lines += [f'<p><strong>Preparation:</strong> {readiness}</p>',
              f'<p>{html_link("Study and practice" if subject["teaching"] else "Study outline", relative_link(source, subject["path"]))}</p>']
    if subject["journey"].get("first_attempt"):
        lines += [f'<p><strong>First attempt:</strong> {escape(subject["journey"]["first_attempt"])}</p>']
    lines += [resource_actions(atlas["resources"][identity], source) for identity in subject["resources"]]
    for identity in subject["technologies"]:
        technology = atlas["technologies"][identity]
        lines += [f'<p>Application: {html_link(technology["title"], relative_link(source, technology["path"]))}</p>']
    return "\n".join(lines + ['</details></li>'])


def teaching_text(root, subject, resources):
    path = root / subject["teaching"]
    text = path.read_text(encoding="utf-8")
    if "\n## Weeks\n" in text:
        text = text.split("\n## Weeks\n", 1)[1]
    else:
        text = "## " + text.split("\n## ", 1)[1]
    text = re.sub(r"^### Week (\d+)", r"### Practice sequence \1", text, flags=re.MULTILINE)
    text = re.sub(r"^(##+) ", r"\1# ", text, flags=re.MULTILINE)

    def relocate(match):
        label, target = match.groups()
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith(("#", "/")):
            return match.group(0)
        destination = path.parent / parsed.path
        link = relative_link(root / subject["path"], destination)
        return f"[{label}]({link}{'#' + parsed.fragment if parsed.fragment else ''})"

    text = re.sub(r"\[([^\]]+)\]\(([^\s)]+)\)", relocate, text)

    def cite(match):
        identity = match.group(1)
        if identity not in resources:
            raise ValueError(f"Unknown teaching source: {identity}")
        title = resources[identity]["title"]
        target = relative_link(subject["path"], f"docs/library/{identity.lower()}.md")
        return f"[{title}]({target})"

    return re.sub(r"`(SRC-[^`]+)`", cite, text)


def render_subject(subject, atlas, root):
    path = subject["path"]
    foundation = subject["foundation"]
    foundation_title = {**atlas["foundations"], **atlas["support_views"]}[foundation]["title"]
    lines = [f"# {subject['title']}", "",
             f"[{foundation_title}](../foundations/{foundation}.md)", ""]
    if subject["journey"].get("question"):
        lines += [f"**{subject['journey']['question']}**", ""]
    lines += ["## What you will develop", "",
              subject.get("exit_capability") or subject["mastery_test"], "",
              "## Before you begin", ""]
    if subject["prerequisites"]:
        lines += ["Recorded prerequisites:", ""]
        lines += [f"- {subject_link(atlas['subjects'][identity], path)}"
                  for identity in subject["prerequisites"]]
    elif "prerequisite_ids" in subject:
        lines += [subject.get("prerequisite_text") or "No subject prerequisite is recorded."]
    else:
        lines += ["Prerequisite guidance has not yet been established for this subject."]
    if subject["journey"].get("first_attempt"):
        lines += ["", "**First attempt:** " + subject["journey"]["first_attempt"]]
    lines += ["", "## Study and practice", ""]
    if subject["teaching"]:
        lines += ["Progress by the work you can do, not by a fixed calendar.", "",
                  teaching_text(root, subject, atlas["resources"])]
        if subject["outcomes"]:
            lines += ["", '??? note "Individual outcomes"', ""]
            for outcome in subject["outcomes"]:
                lines += [f"    ### {outcome['title']} {{#{outcome['id'].lower()}}}", "",
                          "    " + outcome.get("mastery_test", "Assessment not yet specified."), ""]
    else:
        lines += ["This is a study outline. A complete practice sequence is not yet available.", ""]
        concepts = subject.get("core_concepts", [])
        if isinstance(concepts, str):
            lines += [concepts, ""]
        else:
            lines += [f"- {concept}" for concept in concepts]
        for outcome in subject["outcomes"]:
            lines += ["", f"### {outcome['title']} {{#{outcome['id'].lower()}}}", "",
                      outcome.get("mastery_test", "Assessment guidance is not yet recorded.")]
        lines += ["", "### Intended demonstration", "",
                  subject.get("gate") or subject.get("mastery_test", "Not yet specified."), "",
                  "This describes the intended standard, not a validated assessment or a claim of mastery.", ""]
    lines += ["## Reading options", "",
              "Assigned readings, where available, appear in the practice sequence above.",
              "These additional recommendations are not all required reading.", ""]
    for identity in subject["resources"]:
        resource = atlas["resources"][identity]
        direct = any(link["source_id"] == identity and link["target_id"] == subject["id"]
                     for link in subject["recommendations"])
        qualifier = "" if direct else " (recommended for an individual outcome)"
        if resource.get("record_kind") == "reading-area":
            qualifier += " (reading area; selection needed)"
        lines += [f"- [{resource['title']}](../library/{identity.lower()}.md){qualifier}"]
    if not subject["resources"]:
        lines += ["No direct reading recommendation is recorded yet."]
    if subject["technologies"]:
        lines += ["", "## Applications", "", "These are editorial study connections, not compulsory prerequisites.", ""]
        for identity in subject["technologies"]:
            technology = atlas["technologies"][identity]
            connection = next(row for row in technology["study"] if row["subject_id"] == subject["id"])
            lines += [f"- [{technology['title']}]({relative_link(path, technology['path'])}): {connection['rationale']}"]
    lines += ["", "## Continue", ""]
    dependents = [record for record in atlas["subjects"].values()
                  if subject["id"] in record["prerequisites"]]
    lines += ['<div class="atlas-dependencies" markdown>', "",
              '<div markdown>', "", "**Build on**", ""]
    lines += [f"- {subject_link(atlas['subjects'][identity], path)}"
              for identity in subject["prerequisites"]]
    if not subject["prerequisites"]:
        lines += ["No subject prerequisites recorded." if "prerequisite_ids" in subject
                  else "Prerequisites are not established."]
    lines += ["", '</div>', "", '<div markdown>', "", "**This subject**", "",
              subject["title"], "", '</div>', "", '<div markdown>', "", "**Opens into**", ""]
    lines += [f"- {subject_link(record, path)}" for record in dependents]
    if not dependents:
        lines += ["No subsequent dependency is recorded. This does not imply an endpoint."]
    lines += ["", '</div>', "", '</div>', "",
              "Connections above reflect recorded prerequisites, not a compulsory calendar.", ""]
    for identity in subject["journey"].get("connections", []):
        lines += [f"- Related inquiry: {subject_link(atlas['subjects'][identity], path)}"]
    lines += ["", ("[Integrated practice](../praxis/index.md) | "
              "[Choose a study route](../paths/index.md)"), "",
              '??? note "Record and evidence"', "",
              f"    Stable reference: `{subject['id']}`. Documentary availability is not learner mastery.", "",
              ("    [Editorial source record](../09-obelisk/curriculum-index.md#"
              f"{subject['id'].lower()})"), ""]
    return "\n".join(lines)


def render_atlas(root=ROOT):
    atlas = build_atlas(root)
    outputs = {subject["path"]: render_subject(subject, atlas, root)
               for subject in atlas["subjects"].values()}
    outputs.update(render_foundations(atlas))
    outputs.update(render_library(atlas, root))
    outputs.update(render_life(atlas, root))
    outputs.update(render_legacy_routes(atlas, root))
    outputs.update(render_frontier(atlas, root))
    outputs["docs/project/evidence.md"] = render_evidence(atlas, root)
    outputs["data/learner-catalog.json"] = json.dumps(atlas, ensure_ascii=False, indent=2) + "\n"
    return outputs


def render_evidence(atlas, root):
    status = load_json(root, "data/obelisk/release-status.json")
    reviews = load_json(root, "data/obelisk/source-quality.json")["sources"]
    subjects = atlas["subjects"]
    resources = atlas["resources"]
    teaching = sum(bool(subject["teaching"]) for subject in subjects.values())
    reading_areas = sum(resource.get("record_kind") == "reading-area" for resource in resources.values())
    reviewed = len(set(resources) & set(reviews))
    counts = {"Study homes": len(subjects), "Study homes with attached teaching": teaching,
              "Study outlines without an attached practice sequence": len(subjects) - teaching,
              "Identified work/resource records": len(resources) - reading_areas,
              "Reading areas awaiting selection": reading_areas,
              "Source records with individual review notes": reviewed,
              "Source records without individual review notes": len(resources) - reviewed}
    lines = ["# Publication status and evidence", "", f"**Public preview: {status['version']}.**", "",
             "This is an unfinished curriculum and reference project, not a validated qualification or a reference-grade scholarly edition.", "",
             "## What is available", "", "| Inventory | Count |", "| --- | ---: |"]
    lines += [f"| {label} | {count} |" for label, count in counts.items()]
    lines += ["", "Counts describe documentary availability, not teaching quality, independent mastery or unique publications.",
              "Some source records refer to the same work. Individual review notes vary in scope and do not establish complete bibliographic verification.", "",
              "## What the evidence does not establish", "",
              "The imported All Souls prompt mappings are retained for inspection; independent freeze provenance is unverified.",
              "They are not evidence of unseen learner performance, independent examiner acceptance or comparative superiority of Philosophy over other foundations.",
              "No learner-outcome or curriculum-efficacy claim is established by this release. Proposed assessments still need independent calibration and prospective evaluation.", "",
              "The four-foundation organization is an editorial design. Prerequisites, source choices and global coverage still need specialist review.",
              "The developmental routes are examples, not a complete school curriculum. Life-practice material does not replace professional care or advice.", "",
              "## Verification and stewardship", "",
              "Software checks test structure, generation and selected interface behavior. They do not certify scholarship, accessibility or learning outcomes.",
              "Local verification does not establish that a hosted deployment has succeeded.", "",
              "- [Validation methods and claim boundaries](../09-obelisk/validation.md)",
              "- [Source review records](../09-obelisk/source-index.md)",
              "- [Prospective research protocol](../08-research/prospective-validation.md)",
              "- [Report corrections or contribute](../08-community/README.md)", ""]
    return "\n".join(lines)


def render_legacy_routes(atlas, root):
    outputs = {}
    end_marker = "<!-- /atlas-route -->\n\n"
    for subject in atlas["subjects"].values():
        folder = root / "docs/02-knowledge-trunks" / subject["branch_id"].lower()
        matches = list(folder.glob(subject["id"].lower() + "-*.md"))
        if len(matches) > 1:
            raise ValueError(f"Ambiguous legacy route for {subject['id']}")
        if subject["teaching"]:
            matches.append(root / subject["teaching"])
        for path in matches:
            original = path.read_text(encoding="utf-8")
            metadata = {}
            if original.startswith("---\n"):
                header, original = original[4:].split("\n---\n", 1)
                metadata = yaml.safe_load(header) or {}
                original = original.lstrip("\n")
            if end_marker in original:
                original = original.split(end_marker, 1)[1]
            relative = path.relative_to(root).as_posix()
            metadata["search"] = {"exclude": True}
            header = yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True)
            prefix = (f"---\n{header}---\n\n<!-- atlas-route -->\n"
                      f"> **Current study page: {subject_link(subject, relative)}**\n>\n"
                      "> The earlier reference below is retained for continuity.\n" + end_marker)
            outputs[relative] = prefix + original
    return outputs


def render_foundations(atlas):
    outputs = {}
    views = {**atlas["foundations"], **atlas["support_views"]}
    for key, view in views.items():
        path = f"docs/foundations/{key}.md"
        lines = [f"# {view['title']}", "", f"**{view['role']}**", "",
                 f"## {view['question']}", "", view["purpose"], "", "## Starting points", "",
                 "Choose an entry that fits your preparation. This is not a mandatory sequence.", ""]
        for identity in view["entry"]:
            record = atlas["subjects"][identity]
            label = "Study and practice" if record["teaching"] else "Study outline"
            lines += [f"- **{subject_link(record, path)}**. {label}."]
        if key == "capability":
            lines += ["", ("[Seven specializations](../03-specializations/README.md) | "
                      "[Science Fiction to Science](../05-frontier/README.md)")]
        if key == "representation":
            lines += ["", ("Language and literary interpretation sit alongside visual, spatial and "
                      "material representation. Their methods differ; their shared concern is meaningful form.")]
        lines += ["", catalog_controls("subjects", practice=True), "",
                  '<div class="atlas-catalog" data-atlas-catalog markdown>', ""]
        groups = defaultdict(list)
        for subject in atlas["subjects"].values():
            if subject["foundation"] == key:
                group = subject.get("layer") or atlas["branch_labels"].get(subject["branch_id"], "Subjects")
                groups[group].append(subject)
        for group, records in groups.items():
            lines += ["", f"## {group}", "", '<ul class="atlas-rows">']
            lines += [subject_preview(record, atlas, path) for record in records]
            lines += ['</ul>', ""]
        lines += ["", '</div>', "", "## Bring it together", "",
                  ("[A shared-resource inquiry](../praxis/index.md#shared-resource-inquiry) brings "
                  "mechanisms, institutions, judgment and representation into one piece of work."), ""]
        outputs[path] = "\n".join(lines)
    return outputs


def catalog_controls(noun, practice=False, facets=None):
    controls = (
        f'<div class="atlas-filters" data-atlas-controls data-noun="{noun}" hidden>\n'
        f'<label>Find {noun}<input type="search" data-atlas-query aria-controls="atlas-results" '
        'autocomplete="off"></label>\n'
    )
    if practice:
        controls += '<label class="atlas-check"><input type="checkbox" data-atlas-practice> Practice available</label>\n'
        controls += '<label class="atlas-check"><input type="checkbox" data-atlas-resource> Resource link available</label>\n'
    for key, options in (facets or {}).items():
        controls += f'<label>{escape(key.title())}<select data-atlas-filter="{escape(key)}"><option value="">All</option>'
        controls += "".join(f'\n<option value="{escape(value)}">{escape(label)}</option>' for value, label in options)
        controls += '</select></label>\n'
    return controls + '<output id="atlas-results" aria-live="polite"></output>\n</div>'


def render_frontier(atlas, root):
    path = "docs/05-frontier/README.md"
    facets = {"track": [(code, track["name"]) for code, track in atlas["tracks"].items()],
              "class": [(code, f"{code}: {label}") for code, label in atlas["technology_classes"].items()],
              "study": [("mapped", "With study connections"), ("unmapped", "Not mapped yet")]}
    lines = ["# Science Fiction to Science", "", "## 100 technology frontiers and their scientific foundations", "",
             "Explore useful capabilities familiar from science fiction through the science, engineering and courses needed to investigate them.", "",
             "This is a study atlas, not a forecast or a verified ranking of the next inventions. Some capabilities exist; others lack a credible mechanism.", "",
             "Investigate what limits a technology, connect it to foundations, and test your understanding through a concrete piece of work.", "",
             "Classifications are imported, provisional judgments, not independently verified feasibility findings.",
             "Study connections are editorial recommendations. Unmapped technologies have no specific course recommendation yet.", "",
             catalog_controls("technologies", facets=facets), "", '<div class="atlas-catalog" data-atlas-catalog>',
             '<ul class="atlas-rows">']
    outputs = {}
    for technology in atlas["technologies"].values():
        track = atlas["tracks"][technology["track"]]
        entry = track["entry_resource"]
        entry_link = html_link("Introductory track resource", entry["url"]) if entry["url"] else "No track entry URL recorded."
        connections = []
        for row in technology["study"]:
            subject = atlas["subjects"][row["subject_id"]]
            connections += [(f'<p><strong>{html_link(subject["title"], relative_link(path, subject["path"]))}</strong> '
                             f'({escape(row["relationship"])}): {escape(row["rationale"])}</p>')]
            connections += [resource_actions(atlas["resources"][identity], path) for identity in subject["resources"]]
        mapping = "mapped" if technology["study"] else "unmapped"
        lines += [f'<li data-track="{escape(technology["track"])}" data-class="{escape(technology["class"])}" data-study="{mapping}">',
                  '<details class="atlas-preview">',
                  f'<summary><strong>{escape(technology["title"])}</strong><span class="atlas-status">{escape(technology["track"])} / {escape(technology["class"])} / {len(technology["study"])} study connections</span></summary>',
                  f'<p><strong>Bottleneck:</strong> {escape(technology["bottleneck"])}</p>',
                  (f'<p>{html_link(track["name"], "../03-specializations/" + track["path"])}: {entry_link}. '
                   'This is an introduction to the track, not a technology-specific assignment.</p>'),
                  *connections,
                  f'<p><strong>First exercise:</strong> {escape(technology["exercise"])}</p>',
                  f'<p>{html_link("Technology and first exercise", relative_link(path, technology["path"]))}</p>',
                  '</details></li>']
        detail_path = technology["path"]
        original = (root / detail_path).read_text(encoding="utf-8").split("\n<!-- connected-study -->", 1)[0].rstrip()
        original = technology_projection(original, technology, atlas)
        detail = [original, "", "<!-- connected-study -->", "## Connected study", "",
                  atlas["technology_study_policy"], ""]
        for row in technology["study"]:
            subject = atlas["subjects"][row["subject_id"]]
            detail += [f"### {subject_link(subject, detail_path)}", "", f"**{row['relationship'].title()}:** {row['rationale']}", ""]
            detail += [resource_actions(atlas["resources"][identity], detail_path) for identity in subject["resources"]]
        if not technology["study"]:
            detail += ["Specific subject connections have not been mapped yet.", ""]
        detail += ["", f"[Explore technologies]({relative_link(detail_path, path)})", ""]
        outputs[detail_path] = "\n".join(detail)
    lines += ['</ul></div>', ""]
    outputs[path] = "\n".join(lines)
    listings = {"docs/05-frontier/by-track.md": ("Frontier by specialization", [
        (f"{track['name']} {{#{code.lower()}}}", [row for row in atlas["technologies"].values() if row["track"] == code])
        for code, track in atlas["tracks"].items()]),
        "docs/03-specializations/frontier-100.md": ("Frontier technology index", [("Technologies", list(atlas["technologies"].values()))])}
    for code, label in atlas["technology_classes"].items():
        listings[f"docs/05-frontier/class-{code.lower()}.md"] = (
            f"Class {code}: {label}", [("Technologies", [row for row in atlas["technologies"].values() if row["class"] == code])])
    for listing_path, (title, groups) in listings.items():
        listing = ["---", "search:", "  exclude: true", "---", "", f"# {title}", "",
                   f"[Filter technologies and open study resources]({relative_link(listing_path, path)})", "",
                   "Classifications are provisional imported judgments, not independently verified feasibility findings.", ""]
        for heading, records in groups:
            listing += [f"## {heading}", "", f"{len(records)} technologies.", ""]
            for technology in records:
                listing += [(f"- [{technology['title']}]({relative_link(listing_path, technology['path'])}) "
                             f"({technology['track']}, {technology['class']}): {technology['bottleneck']}")]
            listing += [""]
        outputs[listing_path] = "\n".join(listing)
    return outputs


def technology_projection(original, technology, atlas):
    header, body = original[4:].split("\n---\n", 1)
    metadata = yaml.safe_load(header)
    metadata.update({"title": technology["title"], "rank": technology["id"],
                     "feasibility": technology["class"], "primary_track": technology["track"],
                     "secondary_track": technology["secondary"]})
    body = re.sub(r"^# .+$", lambda match: f"# {technology['id']} | {technology['title']}", body, count=1, flags=re.MULTILINE)
    track = atlas["tracks"][technology["track"]]
    track_link = f"[{track['name']}](../../03-specializations/{track['path']})"
    badge = (f'<div class="ofc-tech-meta" markdown>\n\n'
             f'<span class="ofc-badge ofc-{technology["class"].lower()}">{technology["class"]} | {atlas["technology_classes"][technology["class"]]}</span>\n\n'
             f'**Primary track:** {track_link}  \n**Secondary:** {technology["secondary"]}\n\n</div>')
    body = re.sub(r'<div class="ofc-tech-meta" markdown>.*?</div>', lambda match: badge, body, flags=re.DOTALL)
    sections = {"Bottleneck": technology["bottleneck"], "First proof of work": technology["exercise"],
                "Backchain": (f"- **Foundations I:** {technology['foundations']}\n"
                              f"- **Foundations II:** {technology['substrates']}\n"
                              f"- **Specialization:** {track_link}")}
    for heading, content in sections.items():
        body, count = re.subn(rf"^## {heading}\n.*?(?=^## |\Z)",
                             lambda match, replacement=f"## {heading}\n\n{content}\n\n": replacement, body,
                             flags=re.MULTILINE | re.DOTALL)
        if count != 1:
            raise ValueError(f"Expected one {heading} section in technology {technology['id']}")
    return "---\n" + yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True) + "---\n" + body.rstrip()


def render_library(atlas, root):
    quality = load_json(root, "data/obelisk/source-quality.json")["sources"]
    outputs = {}
    index = ["# Library", "", "## Readings and source selection", "",
             ("Reading is part of inquiry, not a completion score. Subject pages distinguish "
             "assigned passages from further reading. Editions, access and scholarly review remain uneven."), "",
             ("Identified works and resources are separate from reading areas that still need a specific selection. "
              "Identification is not bibliographic verification. Some records refer to the same work in different study contexts."), ""]
    for key, foundation in atlas["foundations"].items():
        index += [f"- [{foundation['title']} reading routes](../foundations/{key}.md)"]
    index += ["", catalog_controls("entries"), "",
              '<div class="atlas-catalog" data-atlas-catalog markdown>', ""]
    records = sorted(atlas["resources"].values(), key=lambda row: row["title"].casefold())
    for kind, heading in (("work", "Identified works and resources"),
                          ("reading-area", "Reading areas needing selection")):
        index += [f"## {heading}", ""]
        for record in records:
            if record.get("record_kind", "work") != kind:
                continue
            direct = f" | [Open resource]({record['url']})" if kind == "work" and record.get("url") else ""
            index += [f"- [{record['title']}]({record['id'].lower()}.md){direct}"]
        index += [""]
    for resource in records:
        identity = resource["id"]
        path = f"docs/library/{identity.lower()}.md"
        reading_area = resource.get("record_kind") == "reading-area"
        lines = [f"# {resource['title']}", "", "[Library](index.md)", ""]
        if reading_area:
            lines += ["**Reading area, not a selected publication.**", "",
                      "A specific work, edition or corpus must be selected before this becomes an assigned reading.", ""]
        for field, label in (("author_or_authority", "Author or institution"),
                             ("source_type", "Kind of work"),
                             ("region_or_tradition", "Setting or tradition")):
            if resource.get(field) and not (reading_area and field == "author_or_authority"):
                lines += [f"**{label}:** {resource[field]}", ""]
        if reading_area:
            lines += ["## Selection needed", "", resource.get("edition") or
                      "Choose identifiable works and record the author, title, edition and assigned passages.", ""]
            if resource.get("url"):
                lines += [f"[Starting point for selection]({resource['url']})", "",
                          "This link is a search lead or partial starting point, not a verified reading assignment.", ""]
        elif resource.get("url"):
            lines += [f"[Open the work or publisher record]({resource['url']})", "",
                      "Access may require a library or purchase. The linked edition retains its own rights.", ""]
        else:
            lines += [("An edition and access link have not yet been selected. "
                      "A librarian or qualified guide can help identify a suitable edition."), ""]
        lines += ["## Why investigate it?" if reading_area else "## Why read it?", "", resource.get("use") or
                  "A specific reading purpose has not yet been recorded.", "",
                  "## Reading scope", "", resource.get("reading_mode") or
                  "No passage or chapter assignment is recorded. Consult the associated study route.", "",
                  "## Study connections", ""]
        owners = [subject for subject in atlas["subjects"].values() if identity in subject["resources"]]
        lines += [f"- {subject_link(subject, path)}" for subject in owners]
        if not owners:
            lines += [("No subject-level reading route is attached. "
                      "This record may support a specific outcome or a broader cultural encounter.")]
        review = quality.get(identity, {})
        lines += ["", '??? note "Edition and review notes"', "",
                  "    " + review.get("limitations", "Individual source review is not yet recorded."), "",
                  f"    [Editorial record](../09-obelisk/source-index.md#{identity.lower()})", ""]
        outputs[path] = "\n".join(lines)
    index += ["", '</div>', ""]
    outputs["docs/library/index.md"] = "\n".join(index)
    return outputs


def render_life(atlas, root):
    competencies = load_json(root, "data/obelisk/life-competencies.json")["life_competencies"]
    route_document = load_json(root, "data/obelisk/life-routes.json")
    routes = route_document["routes"]
    scope = load_json(root, "data/obelisk/life-scope.json")["pillars"]
    titles = ["Self and commitments", "Health and care", "Relationships and family",
              "Home and practical independence", "Money and financial decisions",
              "Work and craft", "Communication", "Learning and research",
              "Technology and AI", "Civic and legal life", "Culture and meaning",
              "Nature, place and stewardship"]
    outputs = {}
    index = ["# Life in practice", "", ("Knowledge becomes useful in the situations "
             "you are responsible for. These routes connect study to practice; "
             "they do not replace care, experience or qualified professional help."), ""]
    for number, title in enumerate(titles, 1):
        identity = f"L{number:02d}"
        path = f"docs/life/{identity.lower()}.md"
        index += [f"- [{title}]({identity.lower()}.md)"]
        lines = [f"# {title}", "", "[Life in practice](index.md)", "", "## Readiness and care", ""]
        for label in ("readiness", "scope", "referral", "evidence_boundary"):
            lines += [scope[identity][label], ""]
        for record in competencies:
            if record["Pillar"] != identity:
                continue
            lines += [f"## {record['Competency']} {{#{record['Node'].lower()}}}", "",
                      f"**Understand:** {record['Knowledge to study']}", "",
                      f"**Judge:** {record['Judgment to form']}", "",
                      f"**Practice:** {record['Practice']}", "",
                      f"**Evidence:** {record['Evidence']}", "", "Related study:", ""]
            for target in routes[record["Node"]]:
                lines += [f"- {subject_link(atlas['subjects'][target], path)}"]
            if record["Node"] in route_document["partial_routes"]:
                lines += ["", "**Partial coverage:** " + route_document["partial_routes"][record["Node"]], ""]
        outputs[path] = "\n".join(lines) + "\n"
    outputs["docs/life/index.md"] = "\n".join(index) + "\n"
    return outputs
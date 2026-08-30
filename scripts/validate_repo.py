#!/usr/bin/env python3
from pathlib import Path
import csv, json, re, sys, tomllib

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
errors = []

EXCLUDED_REPO_DIRS = {
    ".git",
    ".venv",
    ".cache",
    ".pytest_cache",
    "__pycache__",
    "archive",
    "node_modules",
    "site",
}


def owned_markdown_files():
    """Yield repository-authored Markdown, not dependencies or build output."""
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if EXCLUDED_REPO_DIRS.intersection(rel.parts):
            continue
        yield path


def is_lfs_pointer(path: Path) -> bool:
    """Return True when checkout left a Git LFS pointer instead of file content."""
    try:
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            return handle.readline().strip() == "version https://git-lfs.github.com/spec/v1"
    except OSError:
        return False

def fail(msg):
    errors.append(msg)

# 1) GitBook summary links must exist.
summary = DOCS / "SUMMARY.md"
if not summary.exists():
    fail("docs/SUMMARY.md missing")
else:
    text = summary.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+\.md)\)", text):
        if target.startswith(("http://","https://")):
            continue
        p = (DOCS / target).resolve()
        if not p.exists():
            fail(f"SUMMARY link missing: {target}")

# 2) Frontier pages and ranks.
frontier_dir = DOCS / "05-frontier" / "technologies"
pages = sorted(frontier_dir.glob("*.md"))
if len(pages) != 100:
    fail(f"Expected 100 frontier technology pages, found {len(pages)}")

ranks = []
classes = set()
tracks = set()
for p in pages:
    txt = p.read_text(encoding="utf-8")
    m_rank = re.search(r"^rank:\s*(\d+)\s*$", txt, re.M)
    m_class = re.search(r'^feasibility:\s*"([^"]+)"\s*$', txt, re.M)
    m_track = re.search(r'^primary_track:\s*"([^"]+)"\s*$', txt, re.M)
    if not (m_rank and m_class and m_track):
        fail(f"Malformed frontier front matter: {p.relative_to(ROOT)}")
        continue
    ranks.append(int(m_rank.group(1)))
    classes.add(m_class.group(1))
    tracks.add(m_track.group(1))

if sorted(ranks) != list(range(1,101)):
    fail("Frontier ranks must be unique 1..100")
if not classes.issubset(set("ABCDE")):
    fail(f"Unexpected feasibility classes: {classes}")
allowed_tracks = {"AI-AS","ROB","ENE","MAT","BIO","NEU","SPA"}
if not tracks.issubset(allowed_tracks):
    fail(f"Unexpected track codes: {tracks}")

# 3) Data counts.
checks = [
    ("data/frontier-100.csv",100),
    ("data/textbook-library-130.csv",130),
    ("data/wave-1-weeks.csv",48),
    ("data/wave-2-weeks.csv",52),
    ("data/wave-4-weeks.csv",12),
]
for rel, expected in checks:
    p=ROOT/rel
    if not p.exists():
        fail(f"Missing {rel}")
        continue
    if is_lfs_pointer(p):
        fail(f"{rel}: Git LFS pointer was not hydrated; CI checkout must run git lfs pull")
        continue
    with p.open(encoding="utf-8-sig", newline="") as f:
        n=sum(1 for _ in csv.DictReader(f))
    if n != expected:
        fail(f"{rel}: expected {expected} rows, found {n}")

# 4) Editorial style surface.
style_guide = ROOT / "STYLE.md"
prose_linter = ROOT / "scripts" / "lint_prose.py"
ui_auditor = ROOT / "scripts" / "audit_ui.py"
if not style_guide.exists():
    fail("STYLE.md missing")
if not prose_linter.exists():
    fail("scripts/lint_prose.py missing")
if not ui_auditor.exists():
    fail("scripts/audit_ui.py missing")
if not (DOCS / "08-community" / "style.md").exists():
    fail("Published writing-style page missing")

# 5) Zensical configuration and explicit nav.
zcfg = ROOT / "zensical.toml"
if not zcfg.exists():
    fail("zensical.toml missing")
else:
    try:
        config = tomllib.loads(zcfg.read_text(encoding="utf-8"))
        project = config.get("project", {})
        if project.get("site_name") != "Open Frontier Curriculum":
            fail("Unexpected or missing Zensical site_name")
        if project.get("docs_dir") != "docs":
            fail("Zensical docs_dir must remain docs")
        if not (DOCS / "02-core" / "README.md").exists():
            fail("Foundations index missing")
        if not (DOCS / "07-resources" / "essential-26.md").exists():
            fail("Essential 26 resource index missing")
        for item in project.get("nav", []):
            values = list(item.values()) if isinstance(item, dict) else [item]
            stack = list(values)
            while stack:
                value = stack.pop()
                if isinstance(value, list):
                    stack.extend(value)
                elif isinstance(value, dict):
                    stack.extend(value.values())
                elif isinstance(value, str) and value.endswith(".md"):
                    if not (DOCS / value).exists():
                        fail(f"Zensical nav target missing: {value}")
    except Exception as exc:
        fail(f"zensical.toml could not be parsed: {exc}")

# GitBook files remain a compatibility surface, not the primary renderer.
cfg = ROOT / ".gitbook.yaml"
if cfg.exists() and "root: ./docs/" not in cfg.read_text(encoding="utf-8"):
    fail(".gitbook.yaml exists but docs root is not configured")


# 5) Walk relative Markdown links across repository Markdown.
for md in owned_markdown_files():
    text = md.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = target.strip().split("#",1)[0]
        if not target or target.startswith(("http://","https://","mailto:","#")):
            continue
        # Ignore non-file pseudo links.
        if "://" in target:
            continue
        p = (md.parent / target).resolve()
        if not p.exists():
            fail(f"Broken Markdown link in {md.relative_to(ROOT)} -> {target}")
            continue
        # Zensical only publishes docs/. Links from a published docs page must
        # not escape that tree even when the target exists in the repository.
        if md.is_relative_to(DOCS) and not p.is_relative_to(DOCS):
            fail(f"Published docs link escapes docs/: {md.relative_to(ROOT)} -> {target}")

# 6) Frozen uv toolchain and critical data/front-matter sync.
pyproject = ROOT / "pyproject.toml"
lockfile = ROOT / "uv.lock"
if not pyproject.exists():
    fail("pyproject.toml missing")
else:
    try:
        pp_text = pyproject.read_text(encoding="utf-8")
        pp = tomllib.loads(pp_text)
        dev = pp.get("dependency-groups", {}).get("dev", [])
        if not any(str(dep).startswith("zensical") for dep in dev):
            fail("Zensical must be declared in the uv dev dependency group")
        if "exclude-newer" in pp_text:
            fail("Do not use a date-based exclude-newer cutoff; reproducibility comes from uv.lock")
    except Exception as exc:
        fail(f"pyproject.toml could not be parsed: {exc}")

if not lockfile.exists():
    fail("uv.lock missing; the documentation toolchain must be committed")
else:
    try:
        lock = tomllib.loads(lockfile.read_text(encoding="utf-8"))
        packages = lock.get("package", [])
        roots = [pkg for pkg in packages if pkg.get("name") == "open-frontier-curriculum-docs"]
        if len(roots) != 1:
            fail("uv.lock must contain exactly one open-frontier-curriculum-docs root package")
        elif roots[0].get("source", {}).get("virtual") != ".":
            fail("open-frontier-curriculum-docs must remain a virtual/non-packaged uv project")
        else:
            project_version = pp.get("project", {}).get("version") if pyproject.exists() else None
            if project_version and roots[0].get("version") != project_version:
                fail(f"uv.lock root version {roots[0].get('version')} does not match pyproject {project_version}")
        zensical = [pkg for pkg in packages if pkg.get("name") == "zensical"]
        if len(zensical) != 1:
            fail("uv.lock must contain exactly one Zensical resolution")
        elif not zensical[0].get("version"):
            fail("uv.lock Zensical package is missing a resolved version")
    except Exception as exc:
        fail(f"uv.lock could not be parsed: {exc}")

ci_workflow = ROOT / ".github" / "workflows" / "ci.yml"
if not ci_workflow.exists():
    fail(".github/workflows/ci.yml missing")
else:
    workflow_text = ci_workflow.read_text(encoding="utf-8")
    for required in [
        "uv sync --frozen",
        "uv run --frozen",
        "scripts/lint_prose.py",
        "scripts/audit_contrast.py",
        "zensical build --clean",
        "python-semantic-release/python-semantic-release",
        "actions/configure-pages",
        "actions/upload-pages-artifact",
        "actions/deploy-pages",
    ]:
        if required not in workflow_text:
            fail(f"ci.yml missing required pipeline step: {required}")

    # Third-party actions are pinned to immutable commit SHAs. This makes the
    # reviewed workflow the code that actually runs. Dependabot can update the
    # pins in a normal pull request.
    for line in workflow_text.splitlines():
        match = re.search(r"\buses:\s+([^\s#]+)", line)
        if not match:
            continue
        action = match.group(1)
        if action.startswith("./"):
            continue
        if not re.fullmatch(r"[^@\s]+@[0-9a-f]{40}", action):
            fail(f"ci.yml action is not pinned to a full commit SHA: {action}")

pr_workflow = ROOT / ".github" / "workflows" / "conventional-pr.yml"
if not pr_workflow.exists():
    fail(".github/workflows/conventional-pr.yml missing")
else:
    pr_text = pr_workflow.read_text(encoding="utf-8")
    if "action-semantic-pull-request" not in pr_text:
        fail("conventional-pr.yml must validate PR titles")
    if "validateSingleCommitMatchesPrTitle: true" not in pr_text:
        fail("conventional-pr.yml must keep single-commit squash messages aligned with PR titles")
    for line in pr_text.splitlines():
        match = re.search(r"\buses:\s+([^\s#]+)", line)
        if not match:
            continue
        action = match.group(1)
        if action.startswith("./"):
            continue
        if not re.fullmatch(r"[^@\s]+@[0-9a-f]{40}", action):
            fail(f"conventional-pr.yml action is not pinned to a full commit SHA: {action}")

# Release metadata is separate from the virtual uv tooling package version.
try:
    release_cfg = tomllib.loads((ROOT / "release.toml").read_text(encoding="utf-8"))
    release_version = release_cfg.get("version", "")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", release_version):
        fail(f"release.toml has invalid semantic version: {release_version!r}")

    citation_text = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    citation_match = re.search(r"(?m)^version:\s*([^\s]+)\s*$", citation_text)
    if not citation_match or citation_match.group(1) != release_version:
        fail("CITATION.cff version must match release.toml")

    program = json.loads((ROOT / "data" / "program.json").read_text(encoding="utf-8"))
    if program.get("version") != release_version:
        fail("data/program.json version must match release.toml")

    if pp.get("project", {}).get("version") != "0.0.0":
        fail("pyproject project.version must stay 0.0.0; repository releases use release.toml")
    semantic = pp.get("tool", {}).get("semantic_release", {})
    if semantic.get("version_toml") != ["release.toml:version"]:
        fail("semantic release must stamp release.toml, not pyproject.toml")
    if set(semantic.get("assets", [])) != {"CITATION.cff", "data/program.json"}:
        fail("semantic release must commit synchronized CITATION.cff and data/program.json assets")
    if semantic.get("allow_zero_version") is not True:
        fail("semantic release must keep 0.x development releases enabled")
    parser_opts = semantic.get("commit_parser_options", {})
    if parser_opts.get("minor_tags") != ["feat"]:
        fail("Conventional release policy must keep feat as the minor-release type")
    expected_patch = {"fix", "perf", "docs", "refactor", "test", "build", "ci", "chore", "style"}
    if set(parser_opts.get("patch_tags", [])) != expected_patch:
        fail("Every accepted non-feat Conventional Commit type must create a patch release")
    if parser_opts.get("other_allowed_tags") not in ([], None):
        fail("Release policy must not accept non-releasing Conventional Commit types")
except Exception as exc:
    fail(f"Could not validate release metadata: {exc}")


start_page = DOCS / "00-start-here" / "README.md"
if start_page.exists():
    start_text = start_page.read_text(encoding="utf-8")
    for target in ["using-ai.md", "execution-modes.md", "first-30-days.md"]:
        if f"]({target})" not in start_text:
            fail(f"Start-here page is missing local link: {target}")
    if '<nav class="ofc-inline-nav"' in start_text:
        fail("Start-here reference links must use native Markdown, not raw-HTML nav wrapping")

frontier_csv = ROOT / "data" / "frontier-100.csv"
if frontier_csv.exists() and not is_lfs_pointer(frontier_csv):
    with frontier_csv.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = [name.strip() for name in (reader.fieldnames or []) if name]
        columns = {name.casefold(): name for name in fieldnames}
        rank_key = columns.get("rank")
        class_key = columns.get("class")
        track_key = columns.get("primary track")

        missing = [
            label
            for label, key in (
                ("Rank", rank_key),
                ("Class", class_key),
                ("Primary track", track_key),
            )
            if key is None
        ]
        if missing:
            fail(
                "data/frontier-100.csv is missing required column(s): "
                + ", ".join(missing)
                + f"; found: {fieldnames}"
            )
            csv_rows = {}
        else:
            csv_rows = {}
            for line_number, row in enumerate(reader, start=2):
                try:
                    rank = int((row.get(rank_key) or "").strip())
                except ValueError:
                    fail(f"data/frontier-100.csv:{line_number}: invalid Rank value")
                    continue
                csv_rows[rank] = row

    for p in pages:
        txt = p.read_text(encoding="utf-8")
        m_rank = re.search(r"^rank:\s*(\d+)\s*$", txt, re.M)
        m_class = re.search(r'^feasibility:\s*"([^"]+)"\s*$', txt, re.M)
        m_track = re.search(r'^primary_track:\s*"([^"]+)"\s*$', txt, re.M)
        if not (m_rank and m_class and m_track):
            continue
        rank = int(m_rank.group(1))
        row = csv_rows.get(rank)
        if not row:
            fail(f"Frontier page rank {rank} missing from CSV")
            continue
        if class_key and row[class_key] != m_class.group(1):
            fail(
                f"Frontier class drift at rank {rank}: "
                f"Markdown={m_class.group(1)} CSV={row[class_key]}"
            )
        if track_key and row[track_key] != m_track.group(1):
            fail(
                f"Frontier track drift at rank {rank}: "
                f"Markdown={m_track.group(1)} CSV={row[track_key]}"
            )

# Do not let copied tracking URLs become canonical curriculum sources.
for md in owned_markdown_files():
    if "utm_source=chatgpt.com" in md.read_text(encoding="utf-8"):
        fail(f"Tracking parameter found in {md.relative_to(ROOT)}")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print("VALIDATION PASSED")
print(f" - {len(pages)} frontier pages")
print(" - ranks 1..100 unique")
print(" - navigation / Markdown links resolve")
print(" - core data row counts match")

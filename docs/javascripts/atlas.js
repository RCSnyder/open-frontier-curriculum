(() => {
  function initializeCatalog() {
    const controls = document.querySelector("[data-atlas-controls]");
    const catalog = document.querySelector("[data-atlas-catalog]");
    if (!controls || !catalog) return;

    const query = controls.querySelector("[data-atlas-query]");
    const practice = controls.querySelector("[data-atlas-practice]");
    const resource = controls.querySelector("[data-atlas-resource]");
    const facets = [...controls.querySelectorAll("[data-atlas-filter]")];
    const output = controls.querySelector("output");
    const rows = [...catalog.querySelectorAll(":scope > ul > li")];

    function filter(save = true) {
      const words = query.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
      let visible = 0;
      for (const row of rows) {
        const text = row.textContent.toLocaleLowerCase();
        const hasPractice = row.dataset.practice === "true";
        row.hidden = !words.every(word => text.includes(word)) || Boolean(practice?.checked && !hasPractice)
          || Boolean(resource?.checked && row.dataset.resource !== "true")
          || facets.some(select => select.value && row.dataset[select.dataset.atlasFilter] !== select.value);
        if (!row.hidden) visible += 1;
      }
      for (const heading of catalog.querySelectorAll("h2")) {
        const list = heading.nextElementSibling;
        heading.hidden = list?.tagName === "UL" && [...list.children].every(row => row.hidden);
      }
      output.textContent = visible ? `${visible} of ${rows.length} ${controls.dataset.noun}` : "No matches";
      if (save) {
        const url = new URL(location.href);
        const values = {find: query.value, practice: practice?.checked ? "1" : "", resource: resource?.checked ? "1" : ""};
        for (const select of facets) values[select.dataset.atlasFilter] = select.value;
        for (const [key, value] of Object.entries(values)) {
          if (value) url.searchParams.set(key, value);
          else url.searchParams.delete(key);
        }
        history.replaceState(history.state, "", url);
      }
    }

    function restore() {
      const params = new URLSearchParams(location.search);
      query.value = params.get("find") || "";
      if (practice) practice.checked = params.get("practice") === "1";
      if (resource) resource.checked = params.get("resource") === "1";
      for (const select of facets) select.value = params.get(select.dataset.atlasFilter) || "";
      filter(false);
    }

    controls.hidden = false;
    query.addEventListener("input", () => filter());
    practice?.addEventListener("change", () => filter());
    resource?.addEventListener("change", () => filter());
    for (const select of facets) select.addEventListener("change", () => filter());
    window.addEventListener("popstate", restore);
    window.addEventListener("pageshow", restore);
    restore();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeCatalog);
  } else {
    initializeCatalog();
  }
})();
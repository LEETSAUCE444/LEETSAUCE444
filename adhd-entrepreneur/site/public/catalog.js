// Catalog filters: show one category at a time. Without JavaScript the chips are
// plain links and every category stays visible.
(function () {
  var chips = Array.prototype.slice.call(document.querySelectorAll(".filter"));
  var cats = Array.prototype.slice.call(document.querySelectorAll(".category"));
  var grid = document.querySelector(".catgrid");

  function show(name) {
    if (!cats.some(function (c) { return c.dataset.cat === name; })) name = "all";
    cats.forEach(function (c) { c.hidden = name !== "all" && c.dataset.cat !== name; });
    if (grid) grid.classList.toggle("solo", name !== "all");
    chips.forEach(function (f) { f.setAttribute("aria-pressed", String(f.dataset.filter === name)); });
  }

  chips.forEach(function (f) {
    f.addEventListener("click", function (e) {
      e.preventDefault();
      var name = f.dataset.filter;
      history.replaceState(null, "", name === "all" ? location.pathname : "#" + name);
      show(name);
      f.scrollIntoView({ block: "nearest", inline: "center", behavior: "smooth" });
    });
  });

  show(location.hash.slice(1) || "all");
})();

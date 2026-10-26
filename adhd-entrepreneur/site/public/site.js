// Split buttons: on click the red, green and blue glass layers slide into line and
// turn white, then the link opens. Skipped for reduced motion and modified clicks.
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".btn-split");
    if (!btn) return;
    btn.classList.remove("merged");
    void btn.offsetWidth; // restart the settle animation
    btn.classList.add("merged");
    setTimeout(function () { btn.classList.remove("merged"); }, 900);

    var href = btn.getAttribute("href");
    if (!href || reduce || e.defaultPrevented) return;
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;
    if (href.charAt(0) === "#" || href.indexOf("mailto:") === 0) return;
    e.preventDefault();
    setTimeout(function () { window.location.href = href; }, 320);
  });
})();

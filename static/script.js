/* ---------------------------------------------------------
   Button "stamps" before the page navigates.
   Works with or without the View Transitions API — if the
   browser supports it, CSS handles the actual page-to-page
   animation (see @view-transition in style.css). This just
   adds the little tactile "thump" on the button itself.
--------------------------------------------------------- */
(function stampAndSubmit() {
  const form = document.getElementById("predict-form");
  const btn = document.getElementById("run-btn");
  if (!form || !btn) return;

  form.addEventListener("submit", (e) => {
    if (btn.classList.contains("stamped")) return; // already submitting
    e.preventDefault();

    btn.classList.add("stamped");
    btn.textContent = "Stamping…";

    window.setTimeout(() => {
      form.submit();
    }, 260);
  });
})();
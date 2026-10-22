// Homepage hero reel: a CSS motion-graphics loop of the four services.
// It can be paused (and stays paused once paused), and it rests whenever it
// is scrolled out of view.
(() => {
  "use strict";

  const reel = document.querySelector("[data-hero-reel]");
  const toggle = reel?.querySelector("[data-reel-toggle]");
  if (!reel || !toggle) return;

  let pausedByUser = false;
  let inView = true;
  const sync = () => reel.classList.toggle("is-paused", pausedByUser || !inView);

  toggle.addEventListener("click", () => {
    pausedByUser = !pausedByUser;
    toggle.setAttribute("aria-pressed", String(pausedByUser));
    toggle.textContent = pausedByUser ? "Play animation" : "Pause animation";
    sync();
  });

  if ("IntersectionObserver" in window) {
    new IntersectionObserver(([entry]) => {
      inView = entry.isIntersecting;
      sync();
    }).observe(reel);
  }
})();

// Insights filter: when a topic is chosen, the articles that remain glide
// into their new places (GSAP Flip) and newly shown articles fade in, so the
// change in the list is easy to follow. Typing in search stays instant.
(() => {
  "use strict";

  const { gsap, Flip } = window;
  if (!gsap || !Flip) return;
  gsap.registerPlugin(Flip);
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  // Called by site.js before it changes which cards are hidden; the returned
  // function runs after the change.
  window.rielartFlip = (targets) => {
    if (reducedMotion.matches) return null;
    const state = Flip.getState(targets);
    return () => Flip.from(state, {
      duration: 0.42,
      ease: "power3.out",
      onEnter: (elements) => gsap.fromTo(elements, { autoAlpha: 0, y: 8 }, { autoAlpha: 1, y: 0, duration: 0.32, ease: "power3.out", clearProps: "opacity,visibility,transform" }),
    });
  };
})();

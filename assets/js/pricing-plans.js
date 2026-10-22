// Pricing: the Services / Extras switch above the plan cards. Without
// JavaScript both groups simply show one after the other.
(() => {
  "use strict";

  const switcher = document.querySelector("[data-plan-switch]");
  if (!switcher) return;
  const tabs = [...switcher.querySelectorAll('[role="tab"]')];
  const panels = tabs.map((tab) => document.getElementById(tab.getAttribute("aria-controls")));
  if (panels.some((panel) => !panel)) return;

  function select(index, focus) {
    tabs.forEach((tab, i) => {
      const selected = i === index;
      tab.setAttribute("aria-selected", String(selected));
      tab.tabIndex = selected ? 0 : -1;
      panels[i].hidden = !selected;
    });
    if (focus) tabs[index].focus();
  }

  tabs.forEach((tab, i) => {
    tab.addEventListener("click", () => select(i));
    tab.addEventListener("keydown", (event) => {
      const last = tabs.length - 1;
      const next = {
        ArrowRight: i === last ? 0 : i + 1,
        ArrowLeft: i === 0 ? last : i - 1,
        Home: 0,
        End: last,
      }[event.key];
      if (next === undefined) return;
      event.preventDefault();
      select(next, true);
    });
  });

  // Links such as /pricing/#business-email-workspace open the group that
  // holds the target, then bring it into view.
  function showHashTarget() {
    let target = null;
    try {
      target = location.hash ? document.getElementById(decodeURIComponent(location.hash.slice(1))) : null;
    } catch (error) {
      target = null;
    }
    const index = target ? panels.findIndex((panel) => panel.contains(target)) : -1;
    if (index < 0) return;
    select(index);
    if (target !== panels[index]) target.scrollIntoView();
  }

  // "Help me choose": one question; CSS shows the matching answer.
  const helpToggle = document.querySelector("[data-plan-help-toggle]");
  const helpPanel = document.getElementById("plan-help");
  if (helpToggle && helpPanel) {
    helpToggle.hidden = false;
    helpToggle.addEventListener("click", () => {
      const open = helpPanel.hidden;
      helpPanel.hidden = !open;
      helpToggle.setAttribute("aria-expanded", String(open));
      if (open) helpPanel.querySelector("input").focus();
    });
  }

  switcher.hidden = false;
  select(0);
  showHashTarget();
  window.addEventListener("hashchange", showHashTarget);
})();

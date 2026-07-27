(() => {
  "use strict";

  const root = document.documentElement;
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const desktopNavigation = window.matchMedia("(min-width: 1081px)");
  root.classList.add("js");

  /* Theme */
  const themeButtons = [...document.querySelectorAll("[data-theme-toggle]")];

  function setTheme(theme, persist = false) {
    const nextTheme = theme === "dark" ? "dark" : "light";
    root.dataset.theme = nextTheme;

    themeButtons.forEach((button) => {
      const nextLabel = nextTheme === "dark" ? "Switch to light mode" : "Switch to dark mode";
      button.setAttribute("aria-label", nextLabel);
      button.setAttribute("aria-pressed", String(nextTheme === "dark"));
    });

    if (persist) {
      try {
        localStorage.setItem("theme", nextTheme);
      } catch (error) {
        /* The theme still works when storage is unavailable. */
      }
    }
  }

  setTheme(root.dataset.theme);
  themeButtons.forEach((button) => {
    button.addEventListener("click", () => {
      setTheme(root.dataset.theme === "dark" ? "light" : "dark", true);
    });
  });

  /* Mobile navigation */
  const menuButton = document.querySelector("[data-menu-toggle]");
  const mobileMenu = document.querySelector("[data-mobile-menu]");
  let previouslyFocused = null;

  function menuFocusableElements() {
    if (!mobileMenu) return [];
    return [...mobileMenu.querySelectorAll("a, button, input, select, textarea, [tabindex]:not([tabindex='-1'])")]
      .filter((element) => !element.hasAttribute("disabled") && !element.hidden);
  }

  function closeMenu({ restoreFocus = true } = {}) {
    if (!menuButton || !mobileMenu) return;
    mobileMenu.classList.remove("open");
    mobileMenu.setAttribute("aria-hidden", "true");
    menuButton.setAttribute("aria-expanded", "false");
    menuButton.setAttribute("aria-label", "Open navigation");
    document.body.classList.remove("menu-open");

    if (restoreFocus && previouslyFocused instanceof HTMLElement) {
      previouslyFocused.focus();
    }
  }

  function openMenu() {
    if (!menuButton || !mobileMenu) return;
    previouslyFocused = document.activeElement;
    mobileMenu.classList.add("open");
    mobileMenu.setAttribute("aria-hidden", "false");
    menuButton.setAttribute("aria-expanded", "true");
    menuButton.setAttribute("aria-label", "Close navigation");
    document.body.classList.add("menu-open");
    menuFocusableElements()[0]?.focus();
  }

  menuButton?.addEventListener("click", () => {
    if (mobileMenu?.classList.contains("open")) {
      closeMenu();
    } else {
      openMenu();
    }
  });

  mobileMenu?.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => closeMenu({ restoreFocus: false }));
  });

  document.addEventListener("keydown", (event) => {
    if (!mobileMenu?.classList.contains("open")) return;

    if (event.key === "Escape") {
      event.preventDefault();
      closeMenu();
      return;
    }

    if (event.key !== "Tab") return;
    const focusable = menuFocusableElements();
    if (!focusable.length) return;
    const first = focusable[0];
    const last = focusable[focusable.length - 1];

    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  });

  const resetMenuForDesktop = (event) => {
    if (event.matches) closeMenu({ restoreFocus: false });
  };

  desktopNavigation.addEventListener?.("change", resetMenuForDesktop);
  resetMenuForDesktop(desktopNavigation);

  /* Accessible homepage priority navigator */
  document.querySelectorAll("[data-hero-system]").forEach((system) => {
    const tabs = [...system.querySelectorAll("[data-hero-topic]")];
    const panels = [...system.querySelectorAll("[data-hero-panel]")];
    const count = system.querySelector("[data-hero-count]");

    function activateHeroTopic(index, { moveFocus = false } = {}) {
      const nextIndex = (index + tabs.length) % tabs.length;

      tabs.forEach((tab, tabIndex) => {
        const isActive = tabIndex === nextIndex;
        tab.setAttribute("aria-selected", String(isActive));
        tab.tabIndex = isActive ? 0 : -1;
      });

      panels.forEach((panel, panelIndex) => {
        panel.hidden = panelIndex !== nextIndex;
      });

      if (count) count.textContent = `${String(nextIndex + 1).padStart(2, "0")} / ${String(tabs.length).padStart(2, "0")}`;
      if (moveFocus) tabs[nextIndex]?.focus();
    }

    tabs.forEach((tab, index) => {
      tab.addEventListener("click", () => activateHeroTopic(index));
      tab.addEventListener("keydown", (event) => {
        let nextIndex = null;

        if (event.key === "ArrowRight" || event.key === "ArrowDown") nextIndex = index + 1;
        if (event.key === "ArrowLeft" || event.key === "ArrowUp") nextIndex = index - 1;
        if (event.key === "Home") nextIndex = 0;
        if (event.key === "End") nextIndex = tabs.length - 1;
        if (nextIndex === null) return;

        event.preventDefault();
        activateHeroTopic(nextIndex, { moveFocus: true });
      });
    });

    const initialIndex = Math.max(0, tabs.findIndex((tab) => tab.getAttribute("aria-selected") === "true"));
    activateHeroTopic(initialIndex);
  });

  /* User-controlled capability marquee */
  document.querySelectorAll("[data-marquee]").forEach((marquee) => {
    const button = marquee.querySelector("[data-marquee-toggle]");
    const label = button?.querySelector("[data-marquee-label]");

    button?.addEventListener("click", () => {
      const paused = marquee.classList.toggle("is-paused");
      button.setAttribute("aria-pressed", String(paused));
      if (label) label.textContent = paused ? "Resume" : "Pause";
    });
  });

  /* Accessible single-open FAQ groups */
  const faqTimers = new WeakMap();

  function answerFor(button) {
    const answerId = button.getAttribute("aria-controls");
    return answerId ? document.getElementById(answerId) : button.closest(".faq-item")?.querySelector(".faq-answer");
  }

  function closeFaq(item, immediate = false) {
    const button = item?.querySelector("[data-faq-question]");
    const answer = button ? answerFor(button) : null;
    if (!button || !answer) return;

    const existingTimer = faqTimers.get(answer);
    if (existingTimer) window.clearTimeout(existingTimer);

    item.classList.remove("open");
    button.setAttribute("aria-expanded", "false");

    if (immediate || reducedMotion.matches) {
      answer.hidden = true;
      return;
    }

    const timer = window.setTimeout(() => {
      if (!item.classList.contains("open")) answer.hidden = true;
    }, 260);
    faqTimers.set(answer, timer);
  }

  function openFaq(item) {
    const button = item?.querySelector("[data-faq-question]");
    const answer = button ? answerFor(button) : null;
    if (!button || !answer) return;

    const existingTimer = faqTimers.get(answer);
    if (existingTimer) window.clearTimeout(existingTimer);

    answer.hidden = false;
    window.requestAnimationFrame(() => {
      item.classList.add("open");
      button.setAttribute("aria-expanded", "true");
    });
  }

  document.querySelectorAll("[data-faq-question]").forEach((button) => {
    const item = button.closest(".faq-item");
    if (!item) return;

    if (button.getAttribute("aria-expanded") === "true") {
      openFaq(item);
    } else {
      closeFaq(item, true);
    }

    button.addEventListener("click", () => {
      const isOpen = button.getAttribute("aria-expanded") === "true";
      const group = item.closest(".faq-list") || item.closest(".faq-group") || item.parentElement;

      group?.querySelectorAll(".faq-item.open").forEach((otherItem) => {
        if (otherItem !== item) closeFaq(otherItem);
      });

      if (isOpen) {
        closeFaq(item);
      } else {
        openFaq(item);
      }
    });
  });

  /* Restrained reveal behavior with a no-JavaScript fallback in CSS */
  const revealElements = [...document.querySelectorAll(".reveal")];

  if (reducedMotion.matches || !("IntersectionObserver" in window)) {
    revealElements.forEach((element) => element.classList.add("visible"));
  } else {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
    );
    revealElements.forEach((element) => observer.observe(element));
  }

  /* Blog filtering and search */
  const filterButtons = [...document.querySelectorAll("[data-filter]")];
  const filterCards = [...document.querySelectorAll("[data-category]")];
  const blogSearch = document.querySelector("[data-blog-search]");
  const blogStatus = document.querySelector("[data-blog-status]");

  function normalize(value) {
    return String(value || "")
      .trim()
      .toLowerCase()
      .replace(/&/g, "and")
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-|-$/g, "");
  }

  function applyBlogFilters() {
    if (!filterCards.length) return;
    const activeButton = filterButtons.find((button) => button.getAttribute("aria-pressed") === "true")
      || filterButtons.find((button) => button.classList.contains("active"))
      || filterButtons[0];
    const activeFilter = normalize(activeButton?.dataset.filter || "all");
    const query = String(blogSearch?.value || "").trim().toLowerCase();
    let visibleCount = 0;

    filterCards.forEach((card) => {
      const categories = String(card.dataset.category || "")
        .split(/[|,]/)
        .map(normalize)
        .filter(Boolean);
      const matchesCategory = activeFilter === "all" || categories.includes(activeFilter);
      const matchesQuery = !query || card.textContent.toLowerCase().includes(query);
      const visible = matchesCategory && matchesQuery;
      card.hidden = !visible;
      if (visible) visibleCount += 1;
    });

    if (blogStatus) {
      blogStatus.textContent = visibleCount
        ? `${visibleCount} article${visibleCount === 1 ? "" : "s"} shown.`
        : "No articles match those filters.";
    }
  }

  filterButtons.forEach((button, index) => {
    const active = button.classList.contains("active") || (!filterButtons.some((item) => item.classList.contains("active")) && index === 0);
    button.setAttribute("aria-pressed", String(active));

    button.addEventListener("click", () => {
      filterButtons.forEach((item) => {
        item.classList.remove("active");
        item.setAttribute("aria-pressed", "false");
      });
      button.classList.add("active");
      button.setAttribute("aria-pressed", "true");
      applyBlogFilters();
    });
  });

  blogSearch?.addEventListener("input", applyBlogFilters);
  applyBlogFilters();

  /* Native form submission state */
  const contactForms = [...document.querySelectorAll("[data-contact-form]")];
  const invalidFormMessage = "Please review the highlighted required fields.";
  const invalidStatusFrames = new WeakMap();

  function requestedInquiryIntent() {
    try {
      const intent = normalize(new URLSearchParams(window.location.search).get("inquiry"));
      return intent === "project" || intent === "review" ? intent : "";
    } catch (error) {
      return "";
    }
  }

  function applyInquiryIntent(form, intent) {
    if (!intent) return;
    const radios = [...form.querySelectorAll('input[type="radio"][name="inquiry_type"]')];
    const valuePattern = intent === "project"
      ? /(^|-)project(-|$)/
      : /(^|-)(review|audit)(-|$)/;
    const matchingRadio = radios.find((radio) => valuePattern.test(normalize(radio.value)));

    if (matchingRadio) matchingRadio.checked = true;
  }

  function announceInvalidForm(form) {
    if (invalidStatusFrames.has(form)) return;
    const status = form.querySelector("[data-form-status]");
    if (!status) return;

    status.textContent = "";
    const frame = window.requestAnimationFrame(() => {
      status.textContent = invalidFormMessage;
      invalidStatusFrames.delete(form);
    });
    invalidStatusFrames.set(form, frame);
  }

  function clearInvalidFormStatus(form) {
    if (form.querySelector('[aria-invalid="true"]')) return;
    const pendingFrame = invalidStatusFrames.get(form);
    if (pendingFrame !== undefined) {
      window.cancelAnimationFrame(pendingFrame);
      invalidStatusFrames.delete(form);
    }

    const status = form.querySelector("[data-form-status]");
    if (status) status.textContent = "";
  }

  function clearValidControlState(form, control) {
    if (!control.validity?.valid) return;

    if (control instanceof HTMLInputElement && control.type === "radio" && control.name) {
      [...form.elements].forEach((element) => {
        if (element instanceof HTMLInputElement && element.type === "radio" && element.name === control.name) {
          element.removeAttribute("aria-invalid");
        }
      });
    } else {
      control.removeAttribute("aria-invalid");
    }

    clearInvalidFormStatus(form);
  }

  function restoreForm(form) {
    form.removeAttribute("aria-busy");
    const button = form.querySelector('[type="submit"]');
    const status = form.querySelector("[data-form-status]");
    if (button) {
      button.disabled = false;
      if (button.dataset.originalLabel) button.innerHTML = button.dataset.originalLabel;
    }
    if (status) status.textContent = "";
  }

  const inquiryIntent = requestedInquiryIntent();

  contactForms.forEach((form) => {
    applyInquiryIntent(form, inquiryIntent);

    form.addEventListener(
      "invalid",
      (event) => {
        const control = event.target;
        if (!(control instanceof HTMLInputElement || control instanceof HTMLSelectElement || control instanceof HTMLTextAreaElement)) return;
        control.setAttribute("aria-invalid", "true");
        announceInvalidForm(form);
      },
      true
    );

    ["input", "change"].forEach((eventName) => {
      form.addEventListener(eventName, (event) => {
        const control = event.target;
        if (!(control instanceof HTMLInputElement || control instanceof HTMLSelectElement || control instanceof HTMLTextAreaElement)) return;
        clearValidControlState(form, control);
      });
    });

    form.addEventListener("submit", () => {
      const button = form.querySelector('[type="submit"]');
      const status = form.querySelector("[data-form-status]");
      form.setAttribute("aria-busy", "true");

      if (button) {
        button.dataset.originalLabel = button.innerHTML;
        button.disabled = true;
        button.textContent = "Sending…";
      }
      if (status) status.textContent = "Your request is being sent.";
    });
  });

  window.addEventListener("pageshow", () => {
    contactForms.forEach(restoreForm);
  });

  /* Current year, active navigation, and header state */
  document.querySelectorAll("[data-year]").forEach((element) => {
    element.textContent = String(new Date().getFullYear());
  });

  const currentPath = window.location.pathname.replace(/\/index\.html$/, "/");
  document.querySelectorAll(".nav a, .mobile-menu nav > a:not(.btn)").forEach((link) => {
    try {
      const url = new URL(link.href, window.location.origin);
      if (url.origin !== window.location.origin) return;
      const linkPath = url.pathname.replace(/\/index\.html$/, "/");
      const active = linkPath === "/" ? currentPath === "/" : currentPath.startsWith(linkPath);
      if (active) link.setAttribute("aria-current", "page");
    } catch (error) {
      /* Ignore malformed optional links without affecting navigation. */
    }
  });

  const header = document.querySelector(".site-header");
  let headerFrame = 0;

  function updateHeader() {
    header?.classList.toggle("is-scrolled", window.scrollY > 16);
    headerFrame = 0;
  }

  updateHeader();
  window.addEventListener(
    "scroll",
    () => {
      if (!headerFrame) headerFrame = window.requestAnimationFrame(updateHeader);
    },
    { passive: true }
  );
})();

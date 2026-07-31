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
  const desktopDropdowns = [...document.querySelectorAll("[data-nav-dropdown]")];
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

  function closeDropdowns(except = null, restoreFocus = false) {
    desktopDropdowns.forEach((dropdown) => {
      if (dropdown === except || !dropdown.open) return;
      dropdown.removeAttribute("open");
      if (restoreFocus) dropdown.querySelector("summary")?.focus();
    });
  }

  desktopDropdowns.forEach((dropdown) => {
    dropdown.addEventListener("toggle", () => dropdown.open && closeDropdowns(dropdown));
    dropdown.querySelectorAll("a").forEach((link) => link.addEventListener("click", () => closeDropdowns()));
  });

  document.addEventListener("click", (event) => {
    if (!desktopDropdowns.some((dropdown) => dropdown.contains(event.target))) {
      closeDropdowns();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape") return;
    const openDropdown = desktopDropdowns.find((dropdown) => dropdown.open);
    if (!openDropdown) return;
    event.preventDefault();
    closeDropdowns(null, true);
  });

  const resetNavigationForViewport = (event) => {
    if (event.matches) closeMenu({ restoreFocus: false });
    else closeDropdowns();
  };

  desktopNavigation.addEventListener?.("change", resetNavigationForViewport);
  resetNavigationForViewport(desktopNavigation);
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

  function requestedServiceIntent() {
    try {
      const requested = normalize(new URLSearchParams(window.location.search).get("service"));
      const aliases = {
        "brand-website-launch": "brand-website-launch",
        "focused-ads-management": "focused-ads-management",
        "focused-ads": "focused-ads-management",
        "advertising": "focused-ads-management",
        "both": "both-services",
        "both-services": "both-services",
        "not-sure": "not-sure",
        "custom-scope": "not-sure"
      };
      return aliases[requested] || "";
    } catch (error) {
      return "";
    }
  }

  function requestedInquiryContext() {
    try {
      const requested = normalize(new URLSearchParams(window.location.search).get("service"));
      return requested === "custom-scope" ? "Custom scope inquiry" : "";
    } catch (error) {
      return "";
    }
  }

  function applyServiceIntent(form, intent) {
    if (!intent) return;
    const radios = [...form.querySelectorAll('input[type="radio"][name="service_interest"]')];
    const matchingRadio = radios.find((radio) => normalize(radio.dataset.serviceValue) === intent);

    if (matchingRadio) matchingRadio.checked = true;
  }

  function updateAdvertisingFields(form) {
    const fields = form.querySelector("[data-ads-fields]");
    if (!fields) return;

    const selected = form.querySelector('input[type="radio"][name="service_interest"]:checked');
    const selectedValue = normalize(selected?.dataset.serviceValue);
    const shouldShow = selectedValue === "focused-ads-management" || selectedValue === "both-services";

    fields.hidden = !shouldShow;
    fields.querySelectorAll("input, select, textarea").forEach((control) => {
      control.disabled = !shouldShow;
      if (!shouldShow) control.removeAttribute("aria-invalid");
    });
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
    if (form.dataset.submitting === "true") return;
    const pendingFrame = invalidStatusFrames.get(form);
    if (pendingFrame !== undefined) {
      window.cancelAnimationFrame(pendingFrame);
      invalidStatusFrames.delete(form);
    }

    const status = form.querySelector("[data-form-status]");
    if (status) {
      status.textContent = "";
      delete status.dataset.state;
    }
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

  function restoreForm(form, { clearStatus = true } = {}) {
    form.removeAttribute("aria-busy");
    delete form.dataset.submitting;
    const button = form.querySelector('[type="submit"]');
    const status = form.querySelector("[data-form-status]");
    if (button) {
      button.disabled = false;
      if (button.dataset.originalLabel) button.innerHTML = button.dataset.originalLabel;
    }
    if (status && clearStatus) {
      status.textContent = "";
      delete status.dataset.state;
    }
  }

  function setFormStatus(form, message, { focus = false, state = "" } = {}) {
    const status = form.querySelector("[data-form-status]");
    if (!status) return;

    status.textContent = message;
    if (state) status.dataset.state = state;
    else delete status.dataset.state;

    if (focus) status.focus({ preventScroll: true });
  }

  async function readFormspreePayload(response) {
    try {
      return typeof response.json === "function" ? await response.json() : null;
    } catch {
      return null;
    }
  }

  function formspreeErrorMessage(payload) {
    if (Array.isArray(payload?.errors) && payload.errors.length > 0) {
      return "Please review the form details and try again. If the problem continues, email hello@rielart.com.";
    }

    return "We could not send your inquiry right now. Please try again, or email hello@rielart.com.";
  }

  function showContactSuccess(form) {
    const panel = form.closest(".contact-form-panel");
    const formContent = panel?.querySelector("[data-form-content]");
    const successCard = panel?.querySelector("[data-contact-success]");

    if (!formContent || !successCard) return false;

    form.reset();
    updateAdvertisingFields(form);
    restoreForm(form);
    formContent.hidden = true;
    successCard.hidden = false;
    successCard.focus({ preventScroll: true });

    const successBounds = successCard.getBoundingClientRect();
    const headerHeight =
      document.querySelector(".site-header")?.getBoundingClientRect().height || 0;
    if (
      successBounds.top < headerHeight ||
      successBounds.top >= window.innerHeight
    ) {
      successCard.scrollIntoView({ block: "start", behavior: "auto" });
    }

    return true;
  }

  const serviceIntent = requestedServiceIntent();
  const inquiryContext = requestedInquiryContext();

  contactForms.forEach((form) => {
    applyServiceIntent(form, serviceIntent);
    const contextField = form.querySelector("[data-inquiry-context]");
    if (contextField instanceof HTMLInputElement) contextField.value = inquiryContext;
    updateAdvertisingFields(form);

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
        if (control instanceof HTMLInputElement && control.name === "service_interest") {
          updateAdvertisingFields(form);
        }
        clearValidControlState(form, control);
      });
    });

    form.addEventListener("submit", async (event) => {
      event.preventDefault();

      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }

      if (form.dataset.submitting === "true") return;

      const button = form.querySelector('[type="submit"]');
      if (!button) return;

      form.dataset.submitting = "true";
      form.setAttribute("aria-busy", "true");

      if (!button.dataset.originalLabel) {
        button.dataset.originalLabel = button.innerHTML;
      }

      button.disabled = true;
      button.textContent = "Sending…";
      setFormStatus(form, "Your request is being sent.", { state: "sending" });

      try {
        const response = await fetch(form.action, {
          method: form.method,
          body: new FormData(form),
          headers: {
            Accept: "application/json"
          }
        });
        const payload = await readFormspreePayload(response);

        if (!response.ok) {
          restoreForm(form, { clearStatus: false });
          setFormStatus(form, formspreeErrorMessage(payload), {
            focus: true,
            state: "error"
          });
          return;
        }

        if (!showContactSuccess(form)) {
          restoreForm(form, { clearStatus: false });
          setFormStatus(form, "Thank you — your inquiry has been sent.", {
            focus: true,
            state: "success"
          });
        }
      } catch {
        restoreForm(form, { clearStatus: false });
        setFormStatus(
          form,
          "We could not send your inquiry right now. Please try again, or email hello@rielart.com.",
          {
            focus: true,
            state: "error"
          }
        );
      }
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

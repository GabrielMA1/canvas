// Contact form: a short, persistent message under each field that needs
// attention, linked to the field with aria-describedby. The browser's own
// validation bubble disappears after a moment; these stay until the field is
// fixed. site.js keeps handling aria-invalid, submission, and status text.
(() => {
  "use strict";

  const form = document.querySelector("[data-contact-form]");
  if (!form) return;

  function messageFor(control) {
    const { validity, type } = control;
    if (validity.valueMissing) {
      if (type === "radio") return "Choose the service you are interested in, or “I am not sure yet.”";
      if (type === "checkbox") return "Please agree to the privacy terms so RielArt can review your inquiry.";
      if (control instanceof HTMLSelectElement) return "Select an option.";
      if (type === "email") return "Enter your work email.";
      return "This field is required.";
    }
    if (validity.typeMismatch && type === "email") return "Enter an email address such as name@yourcompany.com.";
    if (validity.typeMismatch && type === "url") return "Enter the full address, starting with https://.";
    return control.validationMessage;
  }

  function hostFor(control) {
    return control.type === "radio"
      ? control.closest("fieldset")
      : control.closest(".form-field");
  }

  function controlsFor(control) {
    return control.type === "radio" && control.name
      ? [...form.querySelectorAll(`input[type="radio"][name="${CSS.escape(control.name)}"]`)]
      : [control];
  }

  function setDescribedBy(control, id, add) {
    const tokens = new Set((control.getAttribute("aria-describedby") || "").split(/\s+/).filter(Boolean));
    if (add) tokens.add(id);
    else tokens.delete(id);
    if (tokens.size) control.setAttribute("aria-describedby", [...tokens].join(" "));
    else control.removeAttribute("aria-describedby");
  }

  function show(control) {
    const host = hostFor(control);
    if (!host) return;
    const id = `${control.name || control.id}-error`;
    let message = host.querySelector(":scope > .field-error");
    if (!message) {
      message = document.createElement("p");
      message.className = "field-error";
      message.id = id;
      host.append(message);
    }
    message.textContent = messageFor(control);
    controlsFor(control).forEach((item) => setDescribedBy(item, id, true));
  }

  function clear(control) {
    const host = hostFor(control);
    const message = host?.querySelector(":scope > .field-error");
    if (!message) return;
    controlsFor(control).forEach((item) => setDescribedBy(item, message.id, false));
    message.remove();
  }

  form.addEventListener("invalid", (event) => show(event.target), true);

  ["input", "change"].forEach((type) => {
    form.addEventListener(type, (event) => {
      const control = event.target;
      if (!(control instanceof HTMLInputElement || control instanceof HTMLSelectElement || control instanceof HTMLTextAreaElement)) return;
      if (control.validity.valid) clear(control);
      else if (hostFor(control)?.querySelector(":scope > .field-error")) show(control);
    });
  });

  form.addEventListener("reset", () => {
    form.querySelectorAll("input, select, textarea").forEach(clear);
  });
})();

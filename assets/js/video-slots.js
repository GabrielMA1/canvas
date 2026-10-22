// Ad video slots. Each slot names the file it expects in /videos/. Until that
// file is uploaded the slot shows its placeholder; once the file exists the
// video becomes playable (and starts preloading its first frame) with no code
// change. An optional poster image
// (data-poster) is used when it exists too.
(() => {
  "use strict";

  const exists = (url) => fetch(url, { method: "HEAD", cache: "no-store" })
    .then((response) => response.ok)
    .catch(() => false);

  document.querySelectorAll("[data-video-slot]").forEach((slot) => {
    const video = slot.querySelector("video");
    const source = video?.querySelector("source");
    const status = slot.querySelector("[data-video-status]");
    if (!video || !source) return;

    exists(source.src).then((available) => {
      if (!available) {
        if (status) status.textContent = "Coming soon";
        return;
      }
      slot.classList.add("is-ready");
      video.preload = "metadata";
      if (status) status.textContent = "";
      const poster = slot.dataset.poster;
      if (poster) exists(poster).then((found) => { if (found) video.poster = poster; });
    });
  });
})();

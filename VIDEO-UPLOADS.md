# Uploading RielArt ad videos

The homepage (`/#ad-videos`) and the Ad Videos page (`/services/ad-videos/`) each show three video slots. Until a video file exists, its slot shows a blue “Ad video 01 · Coming soon” placeholder. As soon as you upload a file with the expected name, that slot becomes a playable video on both pages. No code change is needed.

## Where to upload

Upload into the `videos/` folder at the root of the `GabrielMA1/canvas` repository, on the `main` branch. GitHub Pages republishes rielart.com about a minute after each upload.

On github.com:

1. Open the repository and click the `videos` folder.
2. Click **Add file → Upload files**.
3. Drag in your files, named exactly as below, and click **Commit changes** (commit directly to `main`).

| Slot | Video file (required) | Poster image (optional) |
|---|---|---|
| Ad video 01 | `videos/rielart-ad-01.mp4` | `videos/rielart-ad-01-poster.jpg` |
| Ad video 02 | `videos/rielart-ad-02.mp4` | `videos/rielart-ad-02-poster.jpg` |
| Ad video 03 | `videos/rielart-ad-03.mp4` | `videos/rielart-ad-03-poster.jpg` |

Names are case-sensitive: lowercase, two-digit numbers, `.mp4` and `.jpg`.

## File settings

- **Format:** MP4 with H.264 video and AAC audio (plays in every browser, including iPhone Safari).
- **Size:** keep each file under about 10 MB. GitHub’s web upload accepts up to 25 MB per file; smaller files load faster for visitors.
- **Shape:** vertical 9:16 (for example 1080 × 1920) fits the slots exactly. Square or horizontal videos also work; they are letterboxed on a dark background.
- **Web optimised / “Fast start”:** turn this on when exporting (Premiere: *Fast Start*; HandBrake: *Web Optimized*; CapCut and most phone editors do this automatically) so the first frame appears quickly.
- **Poster (optional):** a JPG still, ideally 1080 × 1920 and under 150 KB, shown before the video plays. Without a poster, browsers show the video’s first frame (iPhone Safari may show a dark frame until play).

## Changing titles or adding more slots

Each slot’s caption (“RielArt ad video 01”) and label (“Internal project · RielArt”) is plain text in `index.html` and `services/ad-videos/index.html`. Search for `rielart-ad-01` to find a slot. To add a fourth video, copy one `<figure class="video-slot" …>` block, change the number in both file names, and add the new path to `PENDING_MEDIA_UPLOADS` in `tools/site_audit.py` so the audit treats it as awaiting upload until the file exists.

Only show videos RielArt made or has permission to use. Client videos need the client’s written permission and should be labelled as client work.

## Checking

After uploading, run `python tools/site_audit.py`: the “ad video awaiting owner upload” warning disappears for each uploaded file.

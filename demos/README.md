# App demo snippets

Real screen recordings of the LAM app, from Chad's Drive folder "App demos"
(https://drive.google.com/drive/folders/1R0XtQnr8c8xTNg5yaPjvFrer39w_PxB3, added Oct 31, 2026).

- `demos/*.mp4`: the full recordings, 720 px wide (fetched by the "Fetch demo" action).
- `clips/demo-*.mp4` + `photos/demo-*.jpg`: ready snippets, 1080x1920, silent, the phone screen low on LAM navy
  with room above it for the card. Use them in a Social Piece like any clip: `photo: demo-<name> | ...` and `clip: demo-<name> | ...`.

| Snippet | Seconds | What it shows | Good for |
|---|---|---|---|
| demo-skin-photo | 5 | Review your photo (a rash photo) | Skin: "one photo" |
| demo-skin-analyzing | 5 | Camera framing the rash, then "Analyzing Skin" | Skin |
| demo-throat-setup | 6 | "Let's get set up" for the throat check, then the camera in the mouth | Throat |
| demo-throat-analyzing | 5 | "Analyzing Throat" | Throat |
| demo-cough-record | 6 | Cough check recording | Cough |
| demo-lung-guide | 6 | "How to check your child's lungs", then placing the phone on the upper back | Lung (Breathing) |
| demo-lung-analyzing | 2.6 | "Analyzing Audio" for the lung check | Lung (Breathing) |
| demo-vitals-record | 6 | Vitals check measuring | Vitals |
| demo-lia-questions | 6 | LIA symptom picker (fever, cough, sore throat...) | LIA, "a few simple questions" |
| demo-growth-chart | 6 | Growth chart: height on her own curve | Growth |
| demo-bloom-card | 6 | "Today's insight is ready", the daily Bloom card | Bloom, milestones |

Rules (never break):
- Never show a result screen that names a condition or gives a verdict (for example "Strep throat unlikely",
  "Pertussis", "Granuloma annulare", "See a doctor within 24 hours"): it reads as a diagnosis. Show the steps
  (photo, questions, recording, analyzing), the next step card only without condition names.
- Never show a real medicine name (the medication log demo shows a real drug name: no snippet from it yet).
- Never the Ear check or Health Story (not live). The Lung check went live Oct 31, 2026: its result screen says "Abnormal sounds", so never show it.
- Child names in the recordings (Monza, James, Jessica, William) are sample profiles; keep them small or out of frame,
  and never say them in words or captions.
- The "Eve" commentary recordings have a voice: snippets are cut silent; never use Eve's voice in a post without Chad's OK.
- New snippet: cut from `demos/<file>.mp4` with ffmpeg: `-an -vf "scale=-2:1380,pad=1080:1920:(ow-iw)/2:420:color=0x0B1F3A,fps=30"`
  (the phone sits low so the card above it never covers the screen), save the first frame as `photos/<key>.jpg`,
  look at every second of it, then add a row here.

Full recordings: bloom_demo, growth_demo, med_tracker_demo, wellness_check (LIA symptom flow), skin_check,
throat_check (landscape, black bars), general_app (vitals, cough, throat, LIA), eve_* (same flows with Eve's voice).

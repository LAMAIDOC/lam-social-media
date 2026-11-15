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
| demo-lia-fever | 5.2 | The same picker from 0.8 s: Fever ticked, then Cough and Sore Throat; no child name, recording dot covered (Nov 8, 2026) | Fever, "tap her symptoms" |
| demo-throat-scan | 3 | Throat check scan from "Throat AI Check" (Videos no commentary): the green guide over an open mouth, progress 25% to 50%; recording dot covered; no result screen (Nov 8, 2026) | Throat, "check her throat" |
| demo-growth-chart | 6 | Growth chart: height on her own curve | Growth |
| demo-bloom-card | 6 | "Today's insight is ready", the daily Bloom card | Bloom, milestones |
| demo-head-check | 2 | Head Check guide from "LAM - Check Reel" with our cast baby's crown (AI photo) inside the real outline and center line; the head tilts gently, the shoulders sway; the LAM letters and the 9:41 clock redrawn; no result screen (Chad, Nov 9, 2026) | Head shape, "one photo of the top of the head" |
| demo-lia-followup | 6 | LIA follow-up from wellness_check 41.5 s: noisy breathing ticked, then "To make sure I've got this right... it can be a sign of something urgent", No, not certain, then "Ok, got it. Now let's look more closely at the fever" (sample name James in the text; recording dot covered; Nov 15, 2026) | LIA, "it asks what a nurse would ask" |
| demo-lia-checks | 6.5 | From wellness_check 128 s: "Based on what you shared... Recommended checks: 3" (Vitals, Cough, Throat), then the Assessment Progress screen 1/3, 2/3, 3/3 (the throat line says "possible strep patterns": a feature description, not a result; sample name James; Nov 15, 2026) | LIA, "it tells you which checks to do" |
| demo-care-next | 4.5 | Vitals care recommendation from general_app 45.5 s: "oxygen level looks reassuring", then "What to do now" (recheck breathing, offer fluids, rest) scrolling to "Get medical care soon if"; stops before the Urgent warning (sample name Jessica; Nov 15, 2026) | Any check, "a clear next step" |
| demo-lia-journey | 10.5 | The whole flow in one clip: symptom picker (demo-lia-fever 0 to 2 s), the follow-up question, Recommended checks, Assessment Progress, the vitals countdown, then the What to do now card (Nov 15, 2026) | LIA, Fever, "from worry to a plan" |

Nov 15, 2026 snippets (demo-lia-followup, demo-lia-checks, demo-care-next, demo-lia-journey): approved by Chad on Nov 15, 2026, sample names and the "strep patterns" line included.

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

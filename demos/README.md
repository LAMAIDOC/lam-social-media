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
| demo-cough-analyze | 6.4 | Cough check from general_app: recording (85 s), Submit Recording (89.6 s), Analyzing Audio (92 s); recording dots covered; no result (Nov 15, 2026) | Cough, "record her cough" |
| demo-cough-result-blurred | 8.9 | demo-cough-analyze plus the Cough Check Result screen (general_app 114.5 s) with every condition name and the sample child name blurred; the bars, "This is not a medical diagnosis" and "Explain my result" stay. Approved by Chad on Nov 15, 2026 as the one exception to the result screen rule: names must stay blurred, never use an unblurred result (Nov 15, 2026) | Cough, "record, then see the result" |
| demo-lia-followup | 6 | LIA follow-up from wellness_check 41.5 s: noisy breathing ticked, then "To make sure I've got this right... it can be a sign of something urgent", No, not certain, then "Ok, got it. Now let's look more closely at the fever" (sample name James in the text; recording dot covered; Nov 15, 2026) | LIA, "it asks what a nurse would ask" |
| demo-lia-checks | 6.5 | From wellness_check 128 s: "Based on what you shared... Recommended checks: 3" (Vitals, Cough, Throat), then the Assessment Progress screen 1/3, 2/3, 3/3 (the throat line says "possible strep patterns": a feature description, not a result; sample name James; Nov 15, 2026) | LIA, "it tells you which checks to do" |
| demo-care-next | 4.5 | Vitals care recommendation from general_app 45.5 s: "oxygen level looks reassuring", then "What to do now" (recheck breathing, offer fluids, rest) scrolling to "Get medical care soon if"; stops before the Urgent warning (sample name Jessica; Nov 15, 2026) | Any check, "a clear next step" |
| demo-lia-journey | 10.5 | The whole flow in one clip: symptom picker (demo-lia-fever 0 to 2 s), the follow-up question, Recommended checks, Assessment Progress, the vitals countdown, then the What to do now card (Nov 15, 2026) | LIA, Fever, "from worry to a plan" |

**Full feature set (Nov 17, 2026, approved by Chad).** One clip per check and feature, also in Chad's Drive folder
"LAM demo clips (ready to use)" (https://drive.google.com/drive/folders/1MuaMUCAr-4sQphd3iuq1Y1czor_OPx9E).
Built by `demos/build_demos.py` (the status bar is cropped off every recording, so no clock, recording dot or
camera light; the sample name on the throat result is covered). Rebuild with `python3 demos/build_demos.py`.

| Snippet | Seconds | What it shows | Good for |
|---|---|---|---|
| demo-check-head | 4.4 | Head scan, then the real **"Developing Well"** result (from the LAM Check Reel, with its phone frame) | Head shape, App first |
| demo-check-throat | 6.8 | Camera in the mouth at 50%, "Analyzing Throat", then the real **"Strep Throat Unlikely"** result (Chad: only this 8 to 15 s part) | Throat, App first |
| demo-check-cough | 12.8 | How to record, recording, Submit, "Analyzing Audio"; no result (it names a condition) | Cough |
| demo-check-vitals | 13.1 | Ready to record, countdown (3x), "Analyzing Vitals", then the care note "oxygen level looks reassuring" (sample name Jessica in the text) | Vitals, fever |
| demo-check-skin | 10.5 | Capture, the abdomen rash photo, "Analyzing Skin"; no result (it names a condition) | Skin, rash |
| demo-check-lung | 10.8 | How to check your child's lungs, then two back positions with countdowns; no result ("Abnormal sounds") | Lung, breathing |
| demo-lia-regular-checkup | 9.8 | LIA "Regular Checkup" intro, then the symptom picker | LIA, checkup |
| demo-lia-to-checks | 10.5 | Symptoms ticked, then Recommended checks: 3, then Assessment Progress | LIA, "it tells you what to check" |
| demo-lia-throat-questions | 8 | LIA sore throat questions (white spots, swollen tonsils, sore neck) | Throat, LIA |
| demo-lia-bloom-chat | 6.7 | LIA explaining a Bloom card (pretend play), with Tell me more and What can I do | LIA, Bloom |
| demo-growth-height | 9 | Growth chart, Add New Height, the new point on her curve | Growth |
| demo-growth-weight | 11 | Add New Weight, the curve and the Weight Growth Log | Growth |
| demo-growth-head | 8.8 | Add New Head Size and the curve | Growth, head |
| demo-milestone-checklist | 8.2 | Milestones by age, ticking Gross Motor milestones | Milestones |
| demo-milestone-congrats | 7.1 | The last milestone ticked, then "Congratulations! All 6 months old milestones are now completed!" | Milestones, proud moment |
| demo-milestone-tracker | 6.8 | "About Milestones Tracker", then the list by age | Milestones |
| demo-bloom-today | 11.8 | "Today's insight is ready", then swiping through the card | Bloom |
| demo-bloom-share | 6.7 | Share Bloom Insights card with colours and share buttons | Bloom, sharing |
| demo-med-add | 13.7 | Add New Medication: Amoxicillin (Oral Liquid), 10 ml, twice a day, first dose 6:00 PM, 7 days, then Review and Save; ends on Med Tracker with the dose listed (med_tracker_v2, Nov 22, 2026) | Medication, "set it up once" |
| demo-med-dose | 8.6 | Med Tracker: Amoxicillin 10 ml at 6:00 PM, then the dose ticked off; holds on the tick (med_tracker_v2, Nov 22, 2026) | Medication |
| demo-med-progress | 7.3 | Med Progress calendar, then the Share Medication Progress card (med_tracker_v2, Nov 22, 2026) | Medication, sharing |

- App first pieces use demo-check-head and demo-check-throat back to back: the two real reassuring results we have.
- The medication clips were remade on Nov 22, 2026 from Chad's new recording (med_tracker_v2: Amoxicillin, a common
  children's antibiotic), replacing the Paxil ones. The old Drive copies are renamed "OLD Paxil - ..."; never use them.
  The recording's iOS share sheet (64-65.5 s) shows personal contacts: never cut from it.
- Sample names (James, Monza, Jessica) stay small in the text, as in the Nov 15 clips; never say them.

Nov 15, 2026 snippets (demo-lia-followup, demo-lia-checks, demo-care-next, demo-lia-journey): approved by Chad on Nov 15, 2026, sample names and the "strep patterns" line included.

Rules (never break):
- Result screens (changed Nov 17, 2026, Chad): reassuring results are fine ("Developing well", "No Strep Throat
  Suspected", "oxygen level looks reassuring"). Never a result that says something is wrong or names a condition the
  child has (for example "Pertussis", "Granuloma annulare", "Abnormal sounds", "See a doctor within 24 hours").
- The medication log is fine to show, real medicine names included (changed Nov 17, 2026, Chad).
- Never the Ear check or Health Story (not live). The Lung check went live Oct 31, 2026: its result screen says "Abnormal sounds", so never show it.
- Child names in the recordings (Monza, James, Jessica, William) are sample profiles; keep them small or out of frame,
  and never say them in words or captions.
- The "Eve" commentary recordings have a voice: snippets are cut silent; never use Eve's voice in a post without Chad's OK.
- New snippet: cut from `demos/<file>.mp4` with ffmpeg: `-an -vf "scale=-2:1380,pad=1080:1920:(ow-iw)/2:420:color=0x0B1F3A,fps=30"`
  (the phone sits low so the card above it never covers the screen), save the first frame as `photos/<key>.jpg`,
  look at every second of it, then add a row here.

Full recordings: bloom_demo, growth_demo, med_tracker_demo, wellness_check (LIA symptom flow), skin_check,
throat_check (landscape, black bars), general_app (vitals, cough, throat, LIA), eve_* (same flows with Eve's voice).
Added Nov 17, 2026: milestone_demo, growth_demo_v2, med_tracker_complete (720 px), check_reel (the LAM Check Reel ad, 4K).
Added Nov 22, 2026: med_tracker_v2 (Chad's "Med Tracker No Audio", 384 px wide, status bar 50 px: CROP_TOP in build_demos.py).

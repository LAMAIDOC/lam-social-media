#!/usr/bin/env python3
"""Build LAM demo clips (1080x1920, silent, phone low on navy) from the app recordings.
Each clip is a list of segments (source, start, end, speed, extra covers)."""
import subprocess, sys, os, json

D = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(D, "..", "clips")
os.makedirs(OUT, exist_ok=True)
REEL = os.path.join(D, "check_reel.mp4")

DOT = "drawbox=x=212:y=30:w=44:h=40:color=black:t=fill"
CROP_TOP = {"med_tracker_v2": 50}  # 384 px wide recording

COVERS = {  # always applied per source (720 px wide coordinates)
    "general_app": [DOT, "drawbox=x=384:y=36:w=36:h=36:color=black:t=fill"],
    "wellness_check": [DOT],
    "skin_check": [DOT, "drawbox=x=384:y=36:w=36:h=36:color=black:t=fill", "delogo=x=522:y=30:w=34:h=36"],
    "lung_check_1": [DOT, "drawbox=x=384:y=36:w=36:h=36:color=black:t=fill", "delogo=x=527:y=32:w=30:h=32"],
    "lung_check_2": [DOT, "drawbox=x=384:y=36:w=36:h=36:color=black:t=fill", "delogo=x=522:y=30:w=34:h=36"],
    "milestone_demo": [ "drawbox=x=222:y=32:w=44:h=40:color=black:t=fill"],
    "growth_demo_v2": [], "bloom_demo": [],
}
NAME_THROAT = "drawbox=x=540:y=738:w=130:h=44:color=white:t=fill"
NAVY = "0x0B1F3A"

CLIPS = {
  # ---------------- checks
  "demo-check-head": [("REEL", 0.5, 3.1, 1, []), ("REELHOLD", 3.0, 2.0, 1, [])],
  "demo-check-throat": [("general_app", 232.5, 235.0, 1, []), ("general_app", 236.0, 243.5, 1, []),
                        ("general_app", 245.0, 247.5, 1, []), ("general_app", 267.0, 270.0, 1, [NAME_THROAT])],
  "demo-check-cough": [("general_app", 76.5, 79.0, 1, []), ("general_app", 80.5, 86.5, 1, []),
                       ("general_app", 88.5, 90.5, 1, []), ("general_app", 92.0, 95.0, 1, [])],
  "demo-check-vitals": [("general_app", 4.0, 6.0, 1, []), ("general_app", 7.0, 23.0, 3, []),
                        ("general_app", 24.0, 27.0, 1, []), ("general_app", 45.5, 49.0, 1, [])],
  "demo-check-skin": [("skin_check", 9.5, 12.0, 1, []), ("skin_check", 51.8, 54.5, 1, []),
                      ("skin_check", 55.0, 57.0, 1, []), ("skin_check", 58.0, 62.0, 1, [])],
  "demo-check-lung": [("lung_check_1", 2.5, 4.5, 1, []), ("lung_check_1", 6.0, 22.0, 3, []),
                      ("lung_check_1", 26.0, 38.0, 3, [])],
  # ---------------- LIA
  "demo-lia-regular-checkup": [("wellness_check", 6.5, 10.5, 1, []), ("wellness_check", 15.0, 21.0, 1, [])],
  "demo-lia-to-checks": [("wellness_check", 15.0, 20.0, 1, []), ("wellness_check", 129.0, 133.0, 1, []),
                         ("wellness_check", 135.0, 137.0, 1, [])],
  "demo-lia-throat-questions": [("wellness_check", 84.0, 96.0, 1.5, [])],
  "demo-lia-bloom-chat": [("bloom_demo", 76.0, 86.0, 1.5, [])],
  # ---------------- growth
  "demo-growth-height": [("growth_demo_v2", 6.0, 9.0, 1, []), ("growth_demo_v2", 12.0, 22.0, 1.6, [])],
  "demo-growth-weight": [("growth_demo_v2", 26.0, 48.0, 2, [])],
  "demo-growth-head": [("growth_demo_v2", 52.0, 66.0, 1.6, [])],
  # ---------------- milestones
  "demo-milestone-checklist": [("milestone_demo", 11.2, 13.0, 1, []), ("milestone_demo", 24.0, 34.0, 1.5, [])],
  "demo-milestone-congrats": [("milestone_demo", 30.0, 38.5, 1.2, [])],
  "demo-milestone-tracker": [("milestone_demo", 14.0, 17.0, 1, []), ("milestone_demo", 18.0, 22.0, 1, [])],
  # ---------------- medication
  # Nov 22, 2026: med clips remade from med_tracker_v2 (Amoxicillin) to replace the Paxil ones
  "demo-med-add": [("med_tracker_v2", 26.0, 32.0, 1.5, []), ("med_tracker_v2", 32.0, 45.0, 2.5, []), ("med_tracker_v2", 45.0, 52.5, 1.5, [])],
  "demo-med-dose": [("med_tracker_v2", 52.0, 57.0, 1, []), ("med_tracker_v2", 72.4, 75.0, 1, [])],
  "demo-med-progress": [("med_tracker_v2", 55.0, 58.0, 1, []), ("med_tracker_v2", 59.3, 63.8, 1, [])],
  # ---------------- Bloom
  "demo-bloom-today": [("bloom_demo", 24.0, 28.0, 1, []), ("bloom_demo", 34.0, 46.0, 1.5, [])],
  "demo-bloom-share": [("bloom_demo", 52.0, 60.0, 1.2, [])],
}

TRIM = {"demo-check-throat": (8, 15)}  # Chad, Nov 17, 2026
HOLD = {"demo-med-dose": 1.2}  # hold the last frame (the ticked dose) this many seconds  # Chad, Nov 17, 2026: only 8 to 15 s of the full flow

def seg_cmd(src, a, b, speed, extra, outp):
    if src == "REEL":
        vf = "crop=1125:2000:508:930,scale=-2:1380"
        inp = ["-ss", str(a), "-t", str(b - a), "-i", REEL]
    elif src == "REELHOLD":
        vf = "crop=1125:2000:508:930,scale=-2:1380,loop=loop=-1:size=1,trim=duration=%s" % b
        inp = ["-ss", str(a), "-i", REEL, "-frames:v", "1000"]
    else:
        covers = COVERS.get(src, []) + extra
        top = CROP_TOP.get(src, 92)  # status bar height in source pixels
        vf = ",".join(extra + [f"crop=iw:ih-{top}:0:{top}", "scale=-2:1380"])
        inp = ["-ss", str(a), "-t", str(b - a), "-i", f"{D}/{src}.mp4"]
    if speed != 1:
        vf += f",setpts=PTS/{speed}"
    vf += f",pad=1080:1920:(ow-iw)/2:420:color={NAVY},fps=30,format=yuv420p,setsar=1"
    return ["ffmpeg", "-v", "error", "-y"] + inp + ["-vf", vf, "-an", "-c:v", "libx264", "-crf", "18", outp]

def build(name, segs):
    parts = []
    for i, s in enumerate(segs):
        p = f"{OUT}/_{name}_{i}.mp4"
        cmd = seg_cmd(*s, p)
        if s[0] == "REELHOLD":
            cmd = [c for c in cmd if c not in ("-frames:v", "1000")]
        subprocess.run(cmd, check=True)
        parts.append(p)
    # crossfade 0.25 s between segments
    if len(parts) == 1:
        os.replace(parts[0], f"{OUT}/{name}.mp4"); return
    durs = [float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]).strip()) for p in parts]
    fc, last, off = [], "[0:v]", 0.0
    for i in range(1, len(parts)):
        off += durs[i - 1] - 0.25
        lab = f"[x{i}]"
        fc.append(f"{last}[{i}:v]xfade=transition=fade:duration=0.25:offset={off:.3f}{lab}")
        last = lab
    cmd = ["ffmpeg", "-v", "error", "-y"]
    for p in parts: cmd += ["-i", p]
    cmd += ["-filter_complex", ";".join(fc), "-map", last, "-an", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", f"{OUT}/{name}.mp4"]
    subprocess.run(cmd, check=True)
    for p in parts: os.remove(p)

only = sys.argv[2:]
for n, s in CLIPS.items():
    if only and n not in only: continue
    build(n, s)
    if n in TRIM:
        a, b = TRIM[n]; f = f"{OUT}/{n}.mp4"; t = f"{OUT}/_{n}_t.mp4"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(a), "-to", str(b), "-i", f, "-an", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", t], check=True)
        os.replace(t, f)
    if n in HOLD:
        f = f"{OUT}/{n}.mp4"; t = f"{OUT}/_{n}_h.mp4"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f, "-vf", f"tpad=stop_mode=clone:stop_duration={HOLD[n]}", "-an", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", t], check=True)
        os.replace(t, f)
    print(n, subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"{OUT}/{n}.mp4"]).decode().strip())

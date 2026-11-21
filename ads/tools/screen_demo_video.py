"""Screen demo video ads in the CHECK - US layout: headline on top, the real app screen in a phone,
side phones peeking (carousel), LAM logo at the bottom, light blue ground. Usage:
python3 build.py <spec.json> <out_prefix>
spec: {"head1": "...", "head2": "...", "sub": "...", "segments": [{"clip": "throat", "start": 0, "dur": 6.8}, ...]}
"""
import json, subprocess, sys, io, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

D = os.path.dirname(os.path.abspath(__file__))
CLIPS = '/home/claude/lam-social-media/clips'
FPS = 30
NAVY = (0, 25, 79)
GRAY = (95, 105, 125)
SLIDE = 0.45  # carousel slide time

# screen rectangles inside the 1080x1920 demo clips
RECT = {'head': (152 + 92, 420 + 62, 606, 1262)}
for c in ('throat', 'skin', 'cough', 'vitals'):
    RECT[c] = (208, 420, 664, 1380)

def font(n, s):
    return ImageFont.truetype(os.path.join(D, n + '.ttf'), s)

def read_frames(clip, start, dur, w, h):
    x, y, cw, ch = RECT[clip]
    # cover-fit the cropped screen into w x h
    sc = max(w / cw, h / ch)
    sw, sh = int(round(cw * sc)), int(round(ch * sc))
    vf = f'crop={cw}:{ch}:{x}:{y},scale={sw}:{sh},crop={w}:{h},fps={FPS}'
    cmd = ['ffmpeg', '-v', 'error', '-ss', str(start), '-t', str(dur), '-i', f'{CLIPS}/demo-check-{clip}.mp4',
           '-vf', vf, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    n = len(raw) // (w * h * 3)
    fr = [Image.frombuffer('RGB', (w, h), raw[i * w * h * 3:(i + 1) * w * h * 3]) for i in range(n)]
    need = int(round(dur * FPS))
    while len(fr) < need:
        fr.append(fr[-1])
    return fr[:need]

def rounded_mask(w, h, r):
    m = Image.new('L', (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), r, fill=255)
    return m

def phone(screen, bezel, radius):
    w, h = screen.size
    P = Image.new('RGBA', (w + 2 * bezel, h + 2 * bezel), (0, 0, 0, 0))
    d = ImageDraw.Draw(P)
    d.rounded_rectangle((0, 0, P.width - 1, P.height - 1), radius + bezel, fill=(18, 18, 22, 255))
    P.paste(screen, (bezel, bezel), rounded_mask(w, h, radius))
    return P

def background(W, H):
    a = np.linspace(0, 1, H)[:, None]
    top, bot = np.array([226, 243, 251]), np.array([246, 250, 253])
    g = (top * (1 - a) + bot * a)
    img = np.repeat(g[:, None, :], W, 1).reshape(H, W, 3).astype('uint8')
    return Image.fromarray(img)

def wrap(d, text, f, maxw):
    lines = _wrap(d, text, f, maxw)
    if len(lines) > 1:  # balance: shrink the width until the line count would grow
        w = maxw
        while w > 200:
            t = _wrap(d, text, f, w - 10)
            if len(t) > len(lines): break
            lines, w = t, w - 10
    return lines

def _wrap(d, text, f, maxw):
    words, lines, cur = text.split(), [], ''
    for wd in words:
        t = (cur + ' ' + wd).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: lines.append(cur); cur = wd
    lines.append(cur)
    return lines

def static_layer(W, H, spec, L):
    B = background(W, H).convert('RGBA')
    d = ImageDraw.Draw(B)
    y = L['head_y']
    f1, f2 = font('montserrat-latin-700-normal', L['h1']), font('montserrat-latin-800-normal', L['h2'])
    for txt, f, col in ((spec.get('head1', ''), f1, NAVY), (spec.get('head2', ''), f2, NAVY)):
        if not txt: continue
        for ln in wrap(d, txt, f, W - 120):
            tw = d.textlength(ln, font=f)
            d.text(((W - tw) / 2, y), ln, font=f, fill=col)
            y += int(f.size * 1.18)
    if spec.get('sub'):
        fs = font('inter-latin-500-normal', L['sub'])
        y += int(L['sub'] * 0.35)
        for ln in wrap(d, spec['sub'], fs, W - 160):
            tw = d.textlength(ln, font=fs)
            d.text(((W - tw) / 2, y), ln, font=fs, fill=GRAY)
            y += int(fs.size * 1.3)
    logo = Image.open(os.path.join(D, 'logo_color.png')).convert('RGBA')
    lw = L['logo_w']; logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
    B.alpha_composite(logo, ((W - lw) // 2, L['logo_y']))
    return B, y

def ease(t):
    return t * t * (3 - 2 * t)

def render(spec, W, H, L, out):
    base, text_bottom = static_layer(W, H, spec, L)
    top = max(L['phone_top'], text_bottom + 30)
    bottom = L['logo_y'] - 40
    sh = bottom - top - 2 * L['bezel']
    sw = int(sh * 0.481)
    segs = spec['segments']
    print('loading clips', flush=True)
    clips = [read_frames(s['clip'], s.get('start', 0), s['dur'], sw, sh) for s in segs]
    sideh = int(sh * 0.78); sidew = int(sideh * 0.481)
    sides = [read_frames(s['clip'], s.get('start', 0) + s['dur'] * 0.5, 1 / FPS, sidew, sideh)[0] for s in segs]
    def side_phone(i):
        p = phone(sides[i % len(sides)], int(L['bezel'] * 0.8), int(sidew * 0.11))
        return p
    sp = [side_phone(i) for i in range(len(segs))]
    total = sum(len(c) for c in clips)
    cx = W // 2
    ph_w = sw + 2 * L['bezel']
    gap = int(ph_w * 0.62)  # where the side phones sit
    sy = top + (sh + 2 * L['bezel'] - sp[0].height) // 2
    proc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                             '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', out + '_silent.mp4'], stdin=subprocess.PIPE)
    shadow = Image.new('RGBA', (ph_w + 80, sh + 2 * L['bezel'] + 80), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle((40, 50, shadow.width - 40, shadow.height - 30), 90, fill=(0, 25, 79, 70))
    shadow = shadow.filter(ImageFilter.GaussianBlur(28))
    for i, fr in enumerate(clips):
        n = len(fr)
        nxt = (i + 1) % len(segs); prv = (i - 1) % len(segs)
        for k in range(n):
            img = base.copy()
            # carousel: slide in during the first SLIDE seconds of each segment (not the first)
            t = k / FPS
            off = 0
            if i > 0 and t < SLIDE:
                off = int((1 - ease(t / SLIDE)) * gap * 1.6)
            # side phones (dimmed), left = previous, right = next
            for j, x in ((prv, cx - gap + off), (nxt, cx + gap + off)):
                p = sp[j].copy()
                dim = Image.new('RGBA', p.size, (226, 243, 251, 90))
                p.alpha_composite(dim)
                img.alpha_composite(p, (x - p.width // 2, sy))
            img.alpha_composite(shadow, (cx + off - shadow.width // 2, top - 40))
            img.alpha_composite(phone(fr[k], L['bezel'], int(sw * 0.11)), (cx + off - ph_w // 2, top))
            proc.stdin.write(img.convert('RGB').tobytes())
    proc.stdin.close(); proc.wait()
    dur = total / FPS
    # music: the CHECK - US soundtrack (same audio as the leader, so the one change stays the one change)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', out + '_silent.mp4', '-stream_loop', '-1', '-i', os.path.join(D, 'music.m4a'),
                    '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-t', f'{dur:.2f}',
                    '-af', f'afade=t=out:st={max(0, dur - 1):.2f}:d=1', '-movflags', '+faststart', out + '.mp4'], check=True)
    os.remove(out + '_silent.mp4')
    print(out, f'{dur:.1f}s')

L916 = dict(head_y=170, h1=74, h2=86, sub=36, phone_top=480, bezel=16, logo_w=320, logo_y=1700)
L45 = dict(head_y=50, h1=56, h2=64, sub=28, phone_top=280, bezel=13, logo_w=240, logo_y=1235)

if __name__ == '__main__':
    spec = json.load(open(sys.argv[1])); out = sys.argv[2]
    which = sys.argv[3] if len(sys.argv) > 3 else 'both'
    if which in ('both', '916'): render(spec, 1080, 1920, L916, out + '_9x16')
    if which in ('both', '45'): render(spec, 1080, 1350, L45, out + '_4x5')

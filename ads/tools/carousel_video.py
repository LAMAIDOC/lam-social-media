"""Carousel cards -> video slideshow (slow push-in, crossfades), 4:5 and 9:16 on LAM navy.
python3 slideshow.py <out_prefix> <card1.png:secs> <card2.png:secs> ...
"""
import sys, subprocess
import numpy as np
from PIL import Image

FPS, XF = 30, 0.45
NAVY = (0, 25, 79)

def load(p, W, H):
    c = Image.open(p).convert('RGB')
    if c.size != (1080, 1350): c = c.resize((1080, 1350), Image.LANCZOS)
    if H == 1350: return c
    bg = Image.new('RGB', (W, H), NAVY)
    y = (H - 1350) // 2
    a = np.asarray(c).astype(float)
    fade = 90  # soften the top edge of photo cards into the navy
    for r in range(fade):
        t = r / fade
        a[r] = a[r] * t + np.array(NAVY) * (1 - t)
    bg.paste(Image.fromarray(a.astype('uint8')), (0, y))
    return bg

def render(out, cards, W, H):
    imgs = [(load(p, W, H), d) for p, d in cards]
    proc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                             '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', out], stdin=subprocess.PIPE)
    def frame(img, t, d):
        z = 1.0 + 0.035 * (t / d)  # slow push-in
        w, h = int(W / z), int(H / z)
        x, y = (W - w) // 2, (H - h) // 2
        return np.asarray(img.crop((x, y, x + w, y + h)).resize((W, H), Image.BILINEAR)).astype(float)
    for i, (img, d) in enumerate(imgs):
        n = int(round(d * FPS))
        for k in range(n):
            t = k / FPS
            f = frame(img, t, d)
            if i + 1 < len(imgs) and t > d - XF:
                a = (t - (d - XF)) / XF
                nxt = frame(imgs[i + 1][0], 0, imgs[i + 1][1])
                f = f * (1 - a) + nxt * a
            proc.stdin.write(f.astype('uint8').tobytes())
    proc.stdin.close(); proc.wait()

if __name__ == '__main__':
    out = sys.argv[1]
    cards = [(a.split(':')[0], float(a.split(':')[1])) for a in sys.argv[2:]]
    render(out + '_4x5_silent.mp4', cards, 1080, 1350)
    render(out + '_9x16_silent.mp4', cards, 1080, 1920)

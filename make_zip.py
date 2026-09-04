"""Rebuild fishing_fever_presskit_images.zip from assets/ (everything except the trailers)."""
import os, zipfile
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "fishing_fever_presskit_images.zip")
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for sub in ("gifs", "screenshots", "logo", "capsules"):
        d = os.path.join(here, "assets", sub)
        for f in sorted(os.listdir(d)):
            z.write(os.path.join(d, f), os.path.join("fishing_fever_presskit", sub, f))
    demo = os.path.join(here, "assets", "demo")
    for f in sorted(os.listdir(demo)):
        if not f.endswith(".mp4"):
            z.write(os.path.join(demo, f), os.path.join("fishing_fever_presskit", "demo", f))
print("wrote", out, round(os.path.getsize(out) / 1e6, 1), "MB")

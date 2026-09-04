# Fishing Fever press kit

Static press kit site for Fishing Fever. Open `index.html` or visit the GitHub Pages URL.

- Demo: https://store.steampowered.com/app/4637320/Fishing_Fever_Demo/
- Full game: https://store.steampowered.com/app/4636700/Fishing_Fever/
- Contact: ahmadmehdawi2013@gmail.com

Everything in `assets/` is free to use for coverage of the game. See the usage rights section on the page.

## Updating

Source assets live in the game project under `StorePage/`. To refresh:
1. Copy new English GIFs/screenshots into `assets/`, keeping the filenames.
2. Re-encode the trailer under 100 MB: `ffmpeg -i in.mp4 -c:v libx264 -preset slow -crf 22 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart assets/trailer/fishing_fever_trailer_1080p.mp4`
3. Rebuild the zip: `python make_zip.py`
4. Commit and push. GitHub Pages redeploys in a minute or two.

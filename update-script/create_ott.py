
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "playlist.m3u"
OUTPUT = ROOT / "playlist-ott.m3u"

content = SOURCE.read_text(encoding="utf-8-sig")
lines = content.splitlines()

result = ["#EXTM3U"]

for line in lines:
    if line.startswith("#EXTM3U"):
        continue
    result.append(line)

OUTPUT.write_text(
    "\n".join(result) + "\n",
    encoding="utf-8"
)

print("Playlist OTT berhasil dibuat!")
print(f"File: {OUTPUT}")

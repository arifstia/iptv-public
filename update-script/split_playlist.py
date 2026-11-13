from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "playlist.m3u"
OUTPUT = ROOT / "playlists"

# Kategori berdasarkan group-title yang sudah ada
GROUP_CATEGORIES = {
    "indonesia": ["Indonesia Channels"],
    "sports": ["SPORTS"],
    "kids": ["Kids Channel"],
    "vod-indo": ["VOD INDO"],
}

# Kategori tambahan berdasarkan nama channel
NAME_CATEGORIES = {
    "indonesia": [
        "Indosiar (Biz)", "TransTV", "Trans7",
        "MOJI", "TVRI NASIONAL", "MDTV NET",
        "Rajawali TV",
    ],
    "news": [
        "CNN Indonesia", "CNBC Indonesia", "TV One",
        "Kompas TV", "TRIBUN NEWS", "RRI NET",
        "BERITA SATU", "Lingkar TV",
    ],
    "kids": [
        "Nickelodeon", "Baby Shark TV", "Moonbug Kids",
    ],
    "sports": [
        "RedBull TV", "FIFA+ US", "Wired 2 Fish",
    ],
    "religion": [
        "MQTV", "RodjaTV", "AL QURAN KAREEM",
    ],
    "documentary": [
        "Love Nature", "Real Wild",
    ],
}

OUTPUT.mkdir(exist_ok=True)

content = SOURCE.read_text(encoding="utf-8-sig")
entries = re.split(r"(?m)(?=^#EXTINF:)", content)

channels = []

for entry in entries:
    if not entry.startswith("#EXTINF:"):
        continue
    channels.append(entry.strip())

# Siapkan seluruh kategori
categories = {
    name: [] for name in
    set(GROUP_CATEGORIES) | set(NAME_CATEGORIES)
}

uncategorized = []

for entry in channels:
    first_line = entry.splitlines()[0]
    group_match = re.search(r'group-title="([^"]*)"', first_line)
    group = group_match.group(1) if group_match else ""

    category_found = None

    # Prioritaskan group-title
    for category, groups in GROUP_CATEGORIES.items():
        if group in groups:
            category_found = category
            break

    # Jika belum ditemukan, cocokkan nama channel
    if category_found is None:
        for category, names in NAME_CATEGORIES.items():
            if any(
                name.casefold() in first_line.casefold()
                for name in names
            ):
                category_found = category
                break

    if category_found:
        categories[category_found].append(entry)
    else:
        uncategorized.append(first_line)

# Tulis semua playlist kategori
for category, selected in sorted(categories.items()):
    output = OUTPUT / f"{category}.m3u"
    output.write_text(
        "#EXTM3U\n" + "\n".join(selected) + "\n",
        encoding="utf-8"
    )
    print(f"{category}.m3u: {len(selected)} channel")

print(f"\nTotal sumber       : {len(channels)}")
print(f"Total terkategori  : {sum(map(len, categories.values()))}")
print(f"Belum terkategori  : {len(uncategorized)}")

if uncategorized:
    print("\nCHANNEL BELUM TERKATEGORI:")
    for channel in uncategorized:
        print(channel)
else:
    print("\nSEMUA CHANNEL SUDAH TERKATEGORI")

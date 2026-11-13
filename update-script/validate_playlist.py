
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FILES = [
    ROOT / "playlist.m3u",
    ROOT / "playlist-ott.m3u",
    *sorted((ROOT / "playlists").glob("*.m3u"))
]

failed = False

for file in FILES:
    if not file.exists():
        print(f"[ERROR] Tidak ditemukan: {file.name}")
        failed = True
        continue

    lines = file.read_text(
        encoding="utf-8-sig"
    ).splitlines()

    if not lines or not lines[0].strip().startswith("#EXTM3U"):
        print(f"[ERROR] Header tidak valid: {file.name}")
        failed = True
        continue

    entries = 0
    errors = 0

    for i, line in enumerate(lines):
        if not line.startswith("#EXTINF:"):
            continue

        entries += 1
        stream_found = False

        for next_line in lines[i + 1:]:
            value = next_line.strip()

            if not value:
                continue

            if value.startswith("#EXTINF:"):
                break

            # Abaikan metadata IPTV
            if value.startswith("#"):
                continue

            if value.startswith(
                ("http://", "https://", "rtmp://",
                 "rtsp://", "udp://")
            ):
                stream_found = True

            break

        if not stream_found:
            errors += 1
            print(
                f"  [ERROR] Channel tanpa URL: "
                f"baris {i + 1}"
            )

    status = "OK" if errors == 0 else "ERROR"

    print(
        f"[{status}] {file.name}: "
        f"{entries} channel, {errors} kesalahan"
    )

    if errors:
        failed = True

print("\n" + (
    "VALIDASI GAGAL"
    if failed else "SEMUA FORMAT PLAYLIST VALID"
))

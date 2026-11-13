🇮🇩 IPTV Public Indonesia

Kumpulan playlist IPTV publik dan referensi Electronic Program Guide (EPG) untuk aplikasi IPTV yang kompatibel dengan format M3U dan XMLTV.

📺 Playlist IPTV

Playlist utama berisi 91 channel.

M3U URL:

https://raw.githubusercontent.com/arifstia/iptv-public/main/playlist.m3u

Playlist OTT:

https://raw.githubusercontent.com/arifstia/iptv-public/main/playlist-ott.m3u

📂 Playlist Berdasarkan Kategori

Semua playlist kategori dapat digunakan secara terpisah.

Kategori| Jumlah Channel| M3U URL
Indonesia| 16| "indonesia.m3u" (https://raw.githubusercontent.com/arifstia/iptv-public/main/playlists/indonesia.m3u)
Sports| 17| "sports.m3u" (https://raw.githubusercontent.com/arifstia/iptv-public/main/playlists/sports.m3u)
Kids| 7| "kids.m3u" (https://raw.githubusercontent.com/arifstia/iptv-public/main/playlists/kids.m3u)
News| 8| "news.m3u" (https://raw.githubusercontent.com/arifstia/iptv-public/main/playlists/news.m3u)
Religion| 3| "religion.m3u" (https://raw.githubusercontent.com/arifstia/iptv-public/main/playlists/religion.m3u)
Documentary| 2| "documentary.m3u" (https://raw.githubusercontent.com/arifstia/iptv-public/main/playlists/documentary.m3u)
VOD Indo| 38| "vod-indo.m3u" (https://raw.githubusercontent.com/arifstia/iptv-public/main/playlists/vod-indo.m3u)

Jumlah kategori: 91 channel.

📅 Electronic Program Guide (EPG)

EPG digunakan untuk menampilkan informasi jadwal program televisi pada aplikasi IPTV yang mendukung XMLTV.

Sumber XMLTV Indonesia:

https://raw.githubusercontent.com/AqFad2811/epg/main/indonesia.xml

File referensi EPG dalam repository:

https://raw.githubusercontent.com/arifstia/iptv-public/main/epg.xml

Catatan: "epg.xml" di repository ini merupakan referensi sumber EPG, bukan file jadwal XMLTV lengkap yang siap digunakan.

📱 Cara Menggunakan

1. Salin URL playlist yang diinginkan.
2. Buka aplikasi IPTV yang mendukung M3U.
3. Pilih opsi tambah playlist melalui URL.
4. Tempel URL playlist.
5. Simpan dan muat playlist.

Untuk EPG, masukkan URL XMLTV pada pengaturan EPG aplikasi IPTV jika didukung.

🛠️ Struktur Repository

iptv-public/
├── README.md
├── playlist.m3u
├── playlist-ott.m3u
├── epg.xml
├── playlists/
│   ├── indonesia.m3u
│   ├── sports.m3u
│   ├── kids.m3u
│   ├── news.m3u
│   ├── religion.m3u
│   ├── documentary.m3u
│   └── vod-indo.m3u
└── update-script/
    ├── split_playlist.py
    ├── create_ott.py
    └── validate_playlist.py

⚙️ Pengelolaan Playlist

Script tersedia untuk membantu pengelolaan playlist:

- "split_playlist.py" — memisahkan playlist berdasarkan kategori.
- "create_ott.py" — membuat file playlist OTT.
- "validate_playlist.py" — memeriksa format playlist dan keberadaan URL stream.

🔄 Pembaruan

Playlist dapat diperbarui melalui repository GitHub ini.

URL Raw akan mengikuti perubahan terbaru pada branch "main".

⚠️ Catatan

- Ketersediaan channel bergantung pada sumber stream masing-masing.
- Tidak semua stream selalu aktif atau dapat diputar di semua aplikasi.
- Dukungan EPG bergantung pada kecocokan "tvg-id" dan aplikasi IPTV.
- Gunakan hanya sumber siaran yang memiliki izin untuk didistribusikan secara publik.

📄 Lisensi dan Penggunaan

Repository ini menyediakan struktur playlist dan referensi sumber untuk penggunaan IPTV.

Hak cipta atas nama channel, logo, program, dan konten siaran tetap dimiliki oleh pemegang hak masing-masing.

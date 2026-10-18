======================================================================
 KAMPUSKITA AI — CARA MENJALANKAN WEBSITE PORTOFOLIO (WINDOWS & MAC)
======================================================================

A. TENTANG APLIKASI
-----------------
KampusKita AI adalah aplikasi web portofolio yang TERINSPIRASI dari paper
"Optimalisasi Layanan Sistem Informasi Mahasiswa dengan Integrasi Telegram:
Chatbot Retrieval-Augmented-Generation berbasis Large Language Model"
(JTIKA, 2025, Lalu Ramdoni Hidayat dkk.).

Website ini adalah IMPLEMENTASI WEB BARU; bukan antarmuka Telegram
penelitian asli dan bukan layanan resmi Universitas Mataram.

Fitur:
- Landing page pastel, responsif, berdesain ramah belajar.
- Chatbot Mimo dengan sumber jawaban yang dapat diperiksa.
- Upload dan hapus PDF/TXT/MD; maksimal 10 MB, PDF maks. 150 halaman.
- Paper penelitian terindeks otomatis ketika pertama dijalankan.
- Mode DEMO dokumen tanpa AI, tetap berfungsi tanpa Ollama.
- Mode AI dengan model bahasa lokal gratis melalui Ollama.
- Kuis interaktif tiga pertanyaan berdasarkan isi paper.
- Optional semantic retrieval menggunakan embedding Ollama.
- Semua data berjalan di KOMPUTER SENDIRI. Belum ada akun/multi-user.

B. YANG HARUS DISIAPKAN
----------------------
1. Komputer Windows 10/11 atau macOS (atau Linux).
2. Python versi 3.10 atau lebih baru (disarankan 3.11 / 3.12).
   Download: https://www.python.org/downloads/
   PENTING untuk Windows: pilih "Add Python to PATH" saat instalasi.
3. Internet saat instalasi paket (dan saat pertama kali mengunduh model).
4. Ruang penyimpanan model AI jika ingin memakai Ollama (beberapa GB).
   Tanpa Ollama pun mode "Document demo" tetap bisa dijalankan.

C. MENJALANKAN TANPA AI — PALING MUDAH, COBA INI DULU
------------------------------------------------------
WINDOWS:
1. Ekstrak file ZIP proyek menjadi satu folder.
2. Masuk ke folder "KampusKita_AI_Portfolio".
3. Klik dua kali "JALANKAN_WINDOWS.bat".
4. Tunggu instalasi paket Python pertama kali (mungkin beberapa menit).
5. Buka Chrome, Edge, atau Firefox di:
       http://127.0.0.1:8000
6. Klik "AI Study Buddy" -> pilih "Document demo" atau "Auto".
7. Tanya: "Jelaskan cara kerja RAG dari dokumen sampai jawaban."
8. Hasil DEMO adalah cuplikan dokumen dan BUKAN respons generatif AI.
9. Untuk berhenti: buka jendela terminal lalu tekan Ctrl+C.

BILA FILE .BAT TIDAK JALAN, IKUTI LANGKAH MANUAL WINDOWS:
Buka folder proyek, klik address bar Explorer, ketik "cmd" lalu Enter.
    py -m venv .venv
    .venv\Scripts\activate.bat
    python -m pip install -r requirements.txt
    python run.py
Kemudian buka http://127.0.0.1:8000

MAC / LINUX:
Buka Terminal, pindah ke folder yang sudah diekstrak:
    cd /lokasi/folder/KampusKita_AI_Portfolio
    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt
    python run.py
Kemudian buka http://127.0.0.1:8000. Hentikan dengan Ctrl+C.
Alternatif: jalankan ./JALANKAN_MAC_LINUX.sh dari terminal.

D. MENGAKTIFKAN AI SUNGGUHAN (LOCAL OLLAMA)
-------------------------------------------
1. Install aplikasi Ollama dari:
       https://ollama.com/download
2. Pastikan Ollama aktif. Pada terminal BARU, jalankan:
       ollama pull llama3.2:3b
   Model ini dipakai untuk MEMBANGKITKAN jawaban dari konteks dokumen.
   Perlu download beberapa GB. CPU tetap bisa digunakan, tetapi lebih lambat.
3. Pastikan Ollama server berjalan:
       ollama serve
   Jika "address already in use", Ollama biasanya sudah berjalan;
   jangan menjalankan server kedua. Biarkan Ollama aktif.
4. Jika website belum aktif, jalankan lagi langkah C.
5. Di website, klik tombol "Refresh status" di panel kanan.
   Harus muncul: "Your AI is online" / "AI ready".
6. Pilih "Auto (AI when ready)" atau "Local AI" pada chat.
7. Tanya tentang isi paper dan lihat jawaban + referensi sumber.

PENTING:
- Tidak perlu API key, kartu kredit, ataupun paket langganan.
- Ollama berjalan DI PERANGKAT, bukan website publik.
- Jangan unggah dokumen rahasia jika suatu hari website dipublikasikan.
- Jika RAM terbatas, gunakan model lebih kecil seperti llama3.2:1b:
       ollama pull llama3.2:1b
  Windows CMD sebelum python run.py:
       set OLLAMA_CHAT_MODEL=llama3.2:1b
  macOS/Linux sebelum python run.py:
       export OLLAMA_CHAT_MODEL=llama3.2:1b

E. OPSIONAL: SEMANTIC RETRIEVAL DENGAN EMBEDDING
------------------------------------------------
Secara bawaan website memakai TF-IDF (retrieval leksikal) + LLM Ollama.
Ini merupakan ADAPTASI dari paper; paper aslinya menggunakan model
BAAI/bge-base-en-v1.5 dan VectorStoreIndex.

Untuk retrieval semantik lokal, siapkan model embedding:
       ollama pull nomic-embed-text

Lalu aktifkan sebelum menjalankan website, pada terminal yang SAMA:
Windows CMD:
       set USE_OLLAMA_EMBEDDINGS=1
       python run.py
macOS/Linux:
       export USE_OLLAMA_EMBEDDINGS=1
       python run.py

Index embedding awal bisa memerlukan waktu lebih lama karena setiap
potongan teks diubah menjadi vector. Bila gagal, sistem secara otomatis
kembali ke retrieval TF-IDF. Lihat status di panel kanan.

F. CARA MEMAKAI FITUR
---------------------
1. "Overview": pengenalan website dan gambaran alur RAG.
2. "AI Study Buddy": tulis pertanyaan, Enter untuk kirim;
   Shift+Enter untuk baris baru. Pada jawaban AI muncul sumber [S1].
3. "Knowledge Library": klik kotak upload, pilih file PDF/TXT/MD.
   Kembali ke chat dan tanya tentang dokumen tersebut.
4. "Learning Lab": klik Start mini quiz. Kuis ini ditulis dari paper,
   tidak diklaim sebagai pertanyaan yang dihasilkan LLM secara langsung.
5. "Behind the Research": perbandingan metode paper dan web demo.
6. Tombol "Research paper": membuka sumber PDF yang dibundel.
7. Untuk menghapus dokumen unggahan klik tombol "Remove".

PENTING SOAL PDF:
PDF hasil scan/gambar tidak dapat diekstrak tanpa OCR.
Gunakan PDF yang teksnya bisa diseleksi atau ubah ke TXT dahulu.
Pertanyaan tentang peraturan kampus yang tidak tersedia di dokumen
HARUS dikonfirmasi ke kanal akademik resmi.

G. STRUKTUR FOLDER / TEKNOLOGI
------------------------------
run.py                  : memulai server FastAPI / Uvicorn
app/main.py             : endpoint HTTP dan upload dokumen
app/store.py            : ekstraksi PDF, penyimpanan, pembagian chunk
app/rag.py              : TF-IDF, Ollama embeddings opsional, Ollama chat
app/content.py          : ringkasan sumber dan contoh kuis
static/index.html       : antarmuka dan seluruh halaman
static/style.css        : tampilan pastel dan animasi responsif
static/app.js           : interaksi, chat, quiz, unggah dan manajemen dokumen
data/source_paper.pdf   : artikel sumber 11 halaman dari pengguna
data/library.json       : dibuat OTOMATIS saat pertama kali jalan
data/uploads/           : tempat file yang diunggah
requirements.txt        : paket Python

H. ERROR YANG SERING TERJADI
---------------------------
'python' / 'py' not recognized:
  Install Python dan centang Add to PATH, lalu buka ulang CMD.

'No module named ...':
  Aktifkan virtual environment dan jalankan:
      python -m pip install -r requirements.txt

'Address already in use' port 8000:
  Tutup server lama dengan Ctrl+C, atau restart terminal.

'Ollama model offline':
  Pastikan "ollama pull llama3.2:3b" sudah selesai, Ollama aktif,
  lalu tekan Refresh status. Mode demo tetap bekerja tanpa Ollama.

Pertanyaan mengembalikan 'tidak ada sumber':
  Coba pertanyaan lebih spesifik atau unggah dokumen yang relevan.

PDF tidak terbaca:
  Gunakan PDF dengan teks asli, bukan hasil scan. Tidak ada OCR bawaan.

I. CARA MEMASUKKAN KE PORTOFOLIO LAMARAN REVOU
-----------------------------------------------
Saran demo yang direkam:
1. Tunjukkan homepage dan navigasi.
2. Buka Knowledge Library, jelaskan bahwa artikel JTIKA adalah sumber.
3. Tanya chatbot tentang metodologi RAG.
4. Tunjukkan jawaban AI, label model dan kartu sumber.
5. Unggah modul contoh yang memang boleh dibagikan; tanyakan isinya.
6. Tunjukkan Learning Lab sebagai contoh pengalaman pembelajaran.
7. Jelaskan perubahan dari bot Telegram penelitian -> antarmuka web
   yang menekankan transparansi referensi dan UX untuk pembelajar.

Contoh cara mempresentasikan (bahasa Inggris):
"This portfolio is a new web adaptation of my published Telegram RAG
research. I designed the learner-friendly interface, document library,
grounded answer experience, and mini learning activity. Its local LLM
integration uses Ollama. The original study and this new demo use
different retrieval components, which I document transparently."

Jangan mengklaim chatbot pernah digunakan kampus secara luas kalau tidak
ada bukti pengguna atau deployment. Jangan mengklaim 100% general accuracy:
paper hanya mengevaluasi dua pertanyaan sampel dengan kesamaan string.

J. KEAMANAN DAN KETERBATASAN
----------------------------
- Portofolio pengujian lokal; tidak disiapkan untuk hosting publik.
- Tidak ada login, audit keamanan, atau multi-user access control.
- Data disimpan secara lokal, termasuk dokumen pengguna.
- Jangan taruh API key ataupun data mahasiswa yang sensitif di folder.
- AI dapat keliru: cek selalu cuplikan sumber sebelum mengambil keputusan.
- Tidak ada integrasi Telegram langsung pada versi website ini.
- Untuk deploy publik: perlu autentikasi, rate limiting, scanning upload,
  proteksi dokumen, HTTPS, pengamanan prompt injection dan hosting model.

Selamat mencoba! ✿

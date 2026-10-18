"""Seed content derived from published research, not live university policy."""
RESEARCH_BRIEF = """# Panduan penelitian chatbot RAG akademik (ringkasan dari artikel JTIKA)

Judul: Optimalisasi Layanan Sistem Informasi Mahasiswa dengan Integrasi Telegram: Chatbot Retrieval-Augmented-Generation berbasis Large Language Model.
Penulis: Lalu Ramdoni Hidayat, I Gede Pasek Suta Wijaya, Ramaditia Dwiyansaputra. Jurnal Teknologi Informasi, Komputer dan Aplikasinya (JTIKA), Volume 7 Nomor 1, Maret 2025, halaman 121–131.

## Masalah dan tujuan
Mahasiswa Teknik Informatika Universitas Mataram membutuhkan informasi akademik yang mudah diakses tanpa bergantung pada jam operasional staf. Prototipe penelitian mengembangkan chatbot Telegram untuk menjawab pertanyaan akademik berdasarkan dokumen program studi, bukan membuka akses langsung ke sistem akademik produksi.

## Metode penelitian
Pendekatan Research and Development (R&D). Tahapan: identifikasi kebutuhan, survei mahasiswa, pengumpulan dokumen panduan akademik dalam format PDF, preprocessing, pembagian teks menjadi potongan/node, pembentukan indeks pencarian, konfigurasi LLM, integrasi Telegram Bot, pengujian dan evaluasi. Penelitian melaporkan sekitar 40 pertanyaan survei terkait kebutuhan informasi akademik mahasiswa dari sejumlah angkatan.

## Teknologi penelitian asli
Dokumen diproses memakai SimpleDirectoryReader dan SentenceSplitter dengan ukuran chunk 128 token. Embedding memakai BAAI/bge-base-en-v1.5, indeks VectorStoreIndex dan retriever mengambil tiga potongan relevan. Model bahasa yang digunakan pada konfigurasi akhir ialah Zephyr-7B-beta. Integrasi layanan pesan menggunakan python-telegram-bot. Query dipetakan ke representasi, retriever mengambil konteks, LLM menyusun jawaban, lalu bot Telegram mengirim jawaban.

## Pengujian model awal
Paper melaporkan uji awal Meta-Llama-3-8B-Instruct dan Qwen-7B dengan akurasi masing-masing 0,00 dan 0,11 dalam pengujian awal yang didokumentasikan. Evaluasi awal itu menjadi pertimbangan pengembangan RAG. Angka tersebut adalah hasil pengujian lokal dalam artikel, bukan klaim performa umum semua penerapan model.

## Evaluasi dan keterbatasan
Paper melaporkan respons sekitar 60 detik; latensi terkait kebutuhan komputasi GPU dan koneksi stabil. Pengukuran kesesuaian jawaban memakai fuzzy string similarity dengan ambang skor >80. Dua pertanyaan sampel memperoleh 100% pada evaluasi tersebut; hasil ini tidak dapat digeneralisasikan sebagai akurasi 100% untuk semua pertanyaan. Paper menyatakan pertanyaan multi-topik dan variasi pertanyaan masih menjadi keterbatasan, serta menyarankan personalisasi respons dan optimasi performa.

## Apa bedanya situs portofolio ini?
Situs KampusKita AI adalah reimplementasi demonstrasi web yang dibuat setelah penelitian, bukan antarmuka Telegram asli maupun sistem resmi Universitas Mataram. Situs ini dapat mengunggah dokumen PDF/TXT, mengambil potongan sumber relevan, dan memakai model lokal Ollama untuk membuat respons berkonteks. Mode demo tanpa Ollama adalah pencarian dokumen ekstraktif, bukan jawaban generatif AI. Retrieval default menggunakan TF-IDF; retrieval semantic embedding berbasis Ollama opsional. Semua jawaban harus diverifikasi terhadap sumber dan kebijakan resmi.
"""

DEMO_GUIDE = """# Contoh data latihan — BUKAN KEBIJAKAN RESMI KAMPUS
Dokumen ini simulasi untuk memperagakan unggah dan retrieval. Jangan gunakan sebagai rujukan administrasi resmi.

## Program latihan RAG (simulasi)
Contoh bootcamp AI mini terdiri atas tiga sesi. Sesi pertama mempelajari masalah dan tujuan, sesi kedua membangun indexing dan retrieval, sesi ketiga menguji chatbot serta mengevaluasi sumber rujukan. Durasi dan persyaratan kelas ini hanyalah contoh yang dibuat untuk aplikasi portofolio.

## Cara menyiapkan data (simulasi)
Pengajar mengunggah PDF panduan yang telah dibersihkan dari data pribadi. Sistem mengekstrak teks, membagi dokumen menjadi potongan, mencari bagian yang relevan dan mengirim konteks ke LLM lokal.

## Evaluasi kelas (simulasi)
Peserta diminta memeriksa kesesuaian jawaban dengan cuplikan sumber, menandai jawaban yang tidak dapat diverifikasi, dan membandingkan mode demo dengan mode AI. Seluruh aktivitas pada dokumen ini adalah contoh learning activity, bukan hasil penelitian JTIKA.
"""

SUGGESTIONS = [
    "Apa tujuan dan masalah penelitian chatbot ini?",
    "Jelaskan cara kerja RAG dari dokumen sampai jawaban.",
    "Model AI dan embedding apa yang digunakan pada paper?",
    "Bagaimana hasil evaluasi serta keterbatasannya?",
]

QUIZ_OFFLINE = [
    {"question":"Apa fungsi retriever dalam arsitektur RAG?","options":["Mencari potongan dokumen yang relevan","Mengganti Telegram","Menentukan jadwal ujian","Menyimpan kata sandi"],"answer":0,"explanation":"Retriever mengambil bagian dokumen yang relevan untuk menjadi konteks jawaban LLM."},
    {"question":"Bagaimana seharusnya hasil '100%' di paper ditafsirkan?","options":["Akurasi untuk semua pengguna","Kesesuaian pada dua pertanyaan sampel","Garansi bebas halusinasi","Kecepatan respons"],"answer":1,"explanation":"Angka itu berasal dari dua sampel dengan penilaian kemiripan string, bukan jaminan generalisasi."},
    {"question":"Apa keterbatasan yang dibahas pada paper?","options":["Chatbot tidak mendukung teks","Kebutuhan komputasi dan variasi pertanyaan multi-topik","Tidak ada dokumen PDF","Tidak ada integrasi Telegram"],"answer":1,"explanation":"Artikel menyoroti latensi/komputasi dan perlunya peningkatan pemahaman pertanyaan multi-topik."},
]

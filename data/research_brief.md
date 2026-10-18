# Poin metodologi proyek (ringkasan)
Proyek sumber: JTIKA 2025, Lalu Ramdoni Hidayat dkk.
Arsitektur paper: PDF -> SentenceSplitter (128 token) -> embedding BAAI/bge-base-en-v1.5 -> VectorStoreIndex -> retriever -> Zephyr-7B-beta -> Telegram.
Hasil paper: skor kemiripan 100% untuk dua contoh pertanyaan yang dinilai; respons sekitar 60 detik pada pengujian yang dilaporkan. Hasil dua pertanyaan bukan jaminan akurasi umum.
Implementasi situs baru: FastAPI -> TF-IDF retrieval (embedding Ollama opsional) -> Ollama LLM lokal -> web; bukan aplikasi Telegram asli.

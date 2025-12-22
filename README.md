<p align="center">
  <img src="docs/logo.svg" alt="WeaR Ai" width="100" />
</p>

<h1 align="center">WeaR Ai</h1>

<p align="center">
  <strong>🧠 Open Source AI Assistant dengan Pengetahuan Tak Terbatas</strong>
</p>

<p align="center">
  <a href="#fitur">Fitur</a> •
  <a href="#instalasi">Instalasi</a> •
  <a href="#penggunaan">Penggunaan</a> •
  <a href="#teknologi">Teknologi</a>
</p>

---

## ✨ Fitur

- **🧠 Knowledge Monster** — AI dengan basis pengetahuan yang terus berkembang
- **� Bilingual** — Mendukung Bahasa Indonesia dan English
- **💻 Coding Expert** — Ahli dalam Python, JavaScript, dan web development
- **🔍 Smart Search** — Pencarian informasi cerdas
- **📝 Memory System** — Mengingat konteks percakapan
- **⚡ Fast & Local** — Berjalan di komputer Anda sendiri

## 🚀 Instalasi

### Prerequisites
- Python 3.11+
- Node.js 20+
- [Ollama](https://ollama.com) (untuk LLM lokal)

### Quick Start

```bash
# Clone repository
git clone https://github.com/RidTheWann/WeaR-AI.git
cd WeaR-AI

# Setup Backend
cd backend
pip install -e ".[dev]"
cp .env.example .env

# Setup Frontend
cd ../frontend
npm install

# Jalankan
# Terminal 1: Backend
cd backend && python -m uvicorn app.main:app --reload

# Terminal 2: Frontend
cd frontend && npm run dev
```

Buka **http://localhost:3000** 🎉

## 📖 Penggunaan

### Chat dengan AI
Langsung ketik pertanyaan Anda di chat interface. AI akan menjawab dengan:
- Penjelasan yang jelas dan terstruktur
- Contoh kode yang bisa langsung dipakai
- Langkah-langkah yang mudah diikuti

### Contoh Pertanyaan
```
"Jelaskan apa itu recursion dalam programming"
"Buatkan fungsi Python untuk sorting"
"Bagaimana cara deploy aplikasi ke production?"
```

## 🛠️ Teknologi

| Komponen | Teknologi |
|----------|-----------|
| **Frontend** | Next.js 15, React 19, Tailwind CSS |
| **Backend** | Python, FastAPI, LangGraph |
| **AI Engine** | Ollama (Llama, Qwen, dll) |
| **Memory** | Qdrant Vector Database |

## 📁 Struktur Project

```
WeaR-AI/
├── backend/          # FastAPI backend
│   ├── app/
│   │   ├── core/     # AI agent & prompts
│   │   ├── tools/    # AI tools
│   │   └── api/      # REST endpoints
│   └── tests/
├── frontend/         # Next.js frontend
│   └── app/
└── docs/             # Documentation
```

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan:
1. Fork repository ini
2. Buat branch fitur baru
3. Submit pull request

## 📄 Lisensi

MIT License - Bebas digunakan untuk keperluan apapun.

---

<p align="center">
  Made with ❤️ by <strong>RidTheWann</strong>
</p>

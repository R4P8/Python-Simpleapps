# 🛒 SimpleApps — Product Management API

> REST API untuk manajemen produk yang dibangun dengan arsitektur berlapis (*Layered Architecture*) menggunakan pola **Repository-Service-Controller** dan dikontainerisasi dengan **Docker**.

---

## 📋 Daftar Isi

- [Tentang Proyek](#-tentang-proyek)
- [Arsitektur](#-arsitektur)
- [Struktur Folder](#-struktur-folder)
- [Penjelasan Tiap Layer](#-penjelasan-tiap-layer)
- [Teknologi yang Digunakan](#-teknologi-yang-digunakan)
- [Cara Menjalankan](#-cara-menjalankan)
- [Menjalankan dengan Docker](#-menjalankan-dengan-docker)
- [Variabel Lingkungan](#-variabel-lingkungan)
- [API Endpoints](#-api-endpoints)

---

## 📖 Tentang Proyek

**SimpleApps** adalah RESTful API untuk manajemen data produk. Proyek ini menerapkan prinsip ***Separation of Concerns*** melalui arsitektur berlapis sehingga kode menjadi:

- ✅ Lebih **modular** — setiap layer punya tanggung jawab tunggal
- ✅ Lebih mudah **diuji** — tiap layer dapat di-*unit test* secara independen
- ✅ Lebih mudah **dirawat** — perubahan di satu layer tidak merusak layer lain
- ✅ Siap **dikontainerisasi** — tersedia Dockerfile untuk deployment

---

## 🏗️ Arsitektur

Proyek ini mengikuti pola **Repository-Service-Controller**:

```
HTTP Request
     │
     ▼
┌──────────────┐
│   Routes     │  ← Mendefinisikan URL endpoint
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Controller  │  ← Menerima request, mengirim response
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   Service    │  ← Logika bisnis utama
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Repository  │  ← Query langsung ke database
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   Database   │  ← Penyimpanan data via ORM
└──────────────┘
```

---

## 📂 Struktur Folder

```text
.
├── Dockerfile                  # Konfigurasi kontainerisasi Docker
├── Readme.md                   # Dokumentasi utama proyek (file ini)
├── run.py                      # Entry point — menjalankan aplikasi
│
└── app/                        # Direktori utama source code
    ├── __init__.py             # Inisialisasi package Python 'app'
    ├── config.py               # Memuat konfigurasi dari variabel lingkungan
    ├── database.py             # Konfigurasi engine & session database (ORM)
    │
    ├── controllers/            # Layer: penanganan HTTP Request & Response
    │   ├── __init__.py
    │   └── product_controller.py
    │
    ├── models/                 # Layer: skema tabel database (ORM Models)
    │   ├── __init__.py
    │   └── product_model.py
    │
    ├── repositories/           # Layer: operasi CRUD langsung ke database
    │   ├── __init__.py
    │   └── product_repository.py
    │
    ├── routes/                 # Layer: definisi URL endpoint API
    │   ├── __init__.py
    │   └── product_route.py
    │
    └── services/               # Layer: logika bisnis utama (core business logic)
        └── product_service.py
```

---

## 🔍 Penjelasan Tiap Layer

### `run.py` — Entry Point
Titik masuk utama aplikasi. Menginisialisasi server dan memuat seluruh konfigurasi serta komponen aplikasi sebelum mulai menerima request.

---

### `app/config.py` — Konfigurasi
Memuat semua konfigurasi dari variabel lingkungan (`.env`). Menyediakan satu tempat terpusat untuk mengakses pengaturan seperti koneksi database, port, dan mode aplikasi.

---

### `app/database.py` — Koneksi Database
Mengatur *database engine* dan *session* ORM. Menjadi jembatan antara kode Python dan database — semua koneksi dikelola dari sini.

---

### `app/models/` — ORM Models

Mendefinisikan skema tabel database sebagai kelas Python menggunakan ORM.

| File | Tanggung Jawab |
|------|----------------|
| `product_model.py` | Skema tabel `products` (kolom, tipe data, relasi) |

---

### `app/repositories/` — Repository Layer

Satu-satunya layer yang boleh berinteraksi langsung dengan database. Berisi semua operasi CRUD dan query, terisolasi dari logika bisnis.

| File | Tanggung Jawab |
|------|----------------|
| `product_repository.py` | Create, Read, Update, Delete data produk |

---

### `app/services/` — Service Layer

Inti logika bisnis aplikasi. Menerima data dari *repository*, memproses aturan bisnis, lalu mengembalikan hasil ke *controller*. Layer ini tidak tahu cara mengakses database secara langsung.

| File | Tanggung Jawab |
|------|----------------|
| `product_service.py` | Validasi, transformasi, dan aturan bisnis produk |

---

### `app/controllers/` — Controller Layer

Menangani HTTP *request* masuk dan mengirimkan HTTP *response* keluar. Controller tidak mengandung logika bisnis — ia hanya mendelegasikan ke *service* dan memformat response.

| File | Tanggung Jawab |
|------|----------------|
| `product_controller.py` | Parsing request, memanggil service, formatting response |

---

### `app/routes/` — Routes Layer

Menghubungkan URL endpoint ke *controller* yang sesuai. Semua definisi path API didaftarkan di sini.

| File | Tanggung Jawab |
|------|----------------|
| `product_route.py` | Mapping URL `/products` ke product controller |

---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Kegunaan |
|-----------|----------|
| **Python 3.x** | Bahasa pemrograman utama |
| **Flask / FastAPI** | Web framework (sesuaikan dengan yang dipakai) |
| **SQLAlchemy** | ORM untuk interaksi database |
| **Docker** | Kontainerisasi dan deployment |
| **python-dotenv** | Manajemen variabel lingkungan |

---

## 🚀 Cara Menjalankan

### Prasyarat

Pastikan sudah terinstal:
- Python 3.8+
- `pip`

### Langkah-langkah

**1. Clone repositori**
```bash
git clone <url-repositori>
cd simpleapps
```

**2. Buat dan aktifkan virtual environment**
```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Install dependensi**
```bash
pip install -r requirements.txt
```

**4. Salin dan konfigurasi file `.env`**
```bash
cp .env.example .env
# Edit file .env sesuai konfigurasi lokal Anda
```

**5. Jalankan aplikasi**
```bash
python run.py
```

API berjalan di `http://localhost:5000`

---

## 🐳 Menjalankan dengan Docker

**1. Build Docker image**
```bash
docker build -t simpleapps .
```

**2. Jalankan container**
```bash
docker run -p 5000:5000 --env-file .env simpleapps
```

**3. Atau gunakan Docker Compose** *(jika tersedia)*
```bash
docker compose up --build
```

---

## ⚙️ Variabel Lingkungan

Buat file `.env` di root proyek:

```env
# Konfigurasi Database
DATABASE_URL=postgresql://user:password@localhost:5432/simpleapps_db

# Konfigurasi Aplikasi
APP_PORT=5000
APP_DEBUG=True
SECRET_KEY=your-secret-key-here
```

> ⚠️ **Penting:** Jangan pernah meng-*commit* file `.env` ke repositori. Pastikan sudah terdaftar di `.gitignore`.

---

## 📡 API Endpoints

Base URL: `http://localhost:5000`

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| `GET` | `/products` | Mengambil semua data produk |
| `GET` | `/products/{id}` | Mengambil satu produk berdasarkan 

### Contoh Request 

**GET `/products`**
```json
// Response 200 OK
{
  "data": [
    {
      "id": 1,
      "name": "Kemeja Batik",
      "price": 150000,
      "stock": 50
    }
  ],
  "total": 1
}
```

---

## 📄 Lisensi

Proyek ini menggunakan lisensi [MIT](LICENSE).

---

<p align="center">Dibuat dengan ❤️ menggunakan Python</p>
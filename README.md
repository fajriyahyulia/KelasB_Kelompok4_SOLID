# Analisis Prinsip SOLID — Manajemen Kebun Binatang

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-2ECC71?style=flat)
![SOLID](https://img.shields.io/badge/Prinsip-SOLID-1F3864?style=flat)
![Kelas](https://img.shields.io/badge/Kelas-B_Kelompok_4-E67E22?style=flat)

> Pemrograman Berorientasi Objek
> Program Studi Pendidikan Teknik Informatika dan Komputer
> Tahun Akademik 2025/2026

---

## Anggota Kelompok

| NIM | Nama | Bagian |
|---|---|---|
| K3525005 | Fajriyah Yulia Az Zahra | Ketua & Koordinator |
| K3525006 | Fatimah Az Zahra | S — Single Responsibility Principle |
| K3525039 | Riska Nur Rahmawati | O — Open/Closed Principle |
| K3525042 | Vincensius Vicko Riska Saputra | L — Liskov Substitution Principle |
| K3525043 | Wijang Pratama Putra | I — Interface Segregation Principle |
| K3525045 | Abid Satriyo Maulana | D — Dependency Inversion Principle |

---

## Deskripsi Proyek

Repositori ini berisi hasil kerja kelompok dalam menganalisis dan menerapkan prinsip-prinsip **SOLID** pada studi kasus program manajemen **Kebun Binatang** berbasis Python.

Kode awal yang diberikan terdiri dari tiga class (`Hewan`, `Kandang`, `KebunBinatang`) yang dianalisis satu per satu terhadap kelima prinsip SOLID, kemudian dilakukan **refactoring** agar seluruh prinsip terpenuhi.

---

## Struktur Direktori

```
📦 Kelas_B_Kelompok4_SOLID
📁 solusi
   📄 solusi_dip.py
   📄 solusi_isp.py
   📄 solusi_lsp.py
   📄 solusi_ocp.py
   📄 solusi_srp.py
📄 .gitattributes
📄 README.md
📄 analisis.md
📄 kode_awal.py
```

| File/Folder | Keterangan |
|---|---|
| `kode_awal.py` | Kode program original sebelum refactoring |
| `analisis.md` | Penjelasan lengkap analisis & solusi tiap prinsip |
| `solusi/solusi_srp.py` | Refactoring khusus Single Responsibility Principle |
| `solusi/solusi_ocp.py` | Refactoring khusus Open/Closed Principle |
| `solusi/solusi_lsp.py` | Refactoring khusus Liskov Substitution Principle |
| `solusi/solusi_isp.py` | Refactoring khusus Interface Segregation Principle |
| `solusi/solusi_dip.py` | Refactoring khusus Dependency Inversion Principle |

---

## Kode Awal yang Dianalisis

```python
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan.")

    def terbang(self):
        print(f"{self.nama} sedang terbang.")


class Kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")


class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang()

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            hewan.terbang()
```

---

## Hasil Analisis SOLID

### Apakah kode sudah memenuhi semua prinsip SOLID?

> **Belum.** Setelah dianalisis, kode tersebut melanggar hampir semua prinsip SOLID. Tidak ada satu prinsip pun yang terpenuhi secara penuh.

### Ringkasan Status

| Prinsip | Status | Masalah Utama |
|---|---|---|
| **S** — Single Responsibility | Sebagian | `terbang()` tidak relevan untuk semua hewan |
| **O** — Open/Closed | Dilanggar | Harus modifikasi kode lama untuk fitur baru |
| **L** — Liskov Substitution | Dilanggar | Subclass tidak bisa menggantikan parent secara logis |
| **I** — Interface Segregation | Dilanggar | Semua hewan dipaksa punya method `terbang()` |
| **D** — Dependency Inversion | Dilanggar | `KebunBinatang` bergantung pada class konkret |

---

### Analisis Detail per Prinsip

#### S — Single Responsibility Principle *(Sebagian Terpenuhi)*
Pemisahan class secara umum sudah memiliki tujuan masing-masing. Namun, method `terbang()` di dalam class `Hewan` merupakan tanggung jawab yang tidak relevan untuk semua hewan — sapi, ikan, dan singa tetap mewarisi method ini meskipun tidak bisa terbang.

#### O — Open/Closed Principle *(Dilanggar)*
Jika ingin menambahkan perilaku baru (misalnya hewan yang bisa berenang), developer harus memodifikasi langsung method `rawat_semua_hewan()` di class `KebunBinatang`. Sistem belum tertutup untuk modifikasi.

#### L — Liskov Substitution Principle *(Dilanggar)*
Method `rawat_semua_hewan()` memaksa **semua** hewan memanggil `terbang()`. Jika Harimau atau Kura-kura dimasukkan ke `hewan_list`, mereka akan dipaksa "terbang" — yang secara logika sangat keliru dan merusak integritas program.

#### I — Interface Segregation Principle *(Dilanggar)*
Class `Hewan` memiliki method `terbang()` yang memaksa setiap hewan bergantung pada method yang tidak mereka butuhkan. Perilaku `terbang()` seharusnya dipisah ke class tersendiri seperti `BisaTerbang`.

#### D — Dependency Inversion Principle *(Dilanggar)*
Class `KebunBinatang` bergantung langsung pada class konkret `Kandang` melalui `self.kandang = Kandang()` *(tight coupling)*. Seharusnya bergantung pada abstraksi seperti interface `IKandang`.

---

## Solusi Refactoring

Solusi lengkap menggunakan pendekatan berikut:
- **Abstract Base Class (ABC)** untuk mendefinisikan abstraksi
- **Interface terpisah** untuk setiap kemampuan hewan
- **Dependency Injection** pada constructor `KebunBinatang`

```python
from abc import ABC, abstractmethod

# Abstraksi kemampuan (ISP)
class BisaMakan(ABC):
    @abstractmethod
    def makan(self): pass

class BisaTerbang(ABC):
    @abstractmethod
    def terbang(self): pass

class BisaBerenang(ABC):
    @abstractmethod
    def berenang(self): pass

# Hewan hanya berisi atribut dasar (SRP)
class Hewan(BisaMakan):
    def __init__(self, nama):
        self.nama = nama
    def makan(self):
        print(f"{self.nama} sedang makan.")

# Subclass hanya implement kemampuan yang relevan (LSP & ISP)
class Burung(Hewan, BisaTerbang):
    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class Ikan(Hewan, BisaBerenang):
    def berenang(self):
        print(f"{self.nama} sedang berenang.")

# Abstraksi Kandang (DIP)
class IKandang(ABC):
    @abstractmethod
    def tambah_hewan(self, hewan): pass
    @abstractmethod
    def get_semua_hewan(self): pass
    @abstractmethod
    def bersihkan_kandang(self): pass

class Kandang(IKandang):
    def __init__(self):
        self.hewan_list = []
    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)
    def get_semua_hewan(self):
        return self.hewan_list
    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")

# Dependency Injection (DIP)
class KebunBinatang:
    def __init__(self, kandang: IKandang):
        self.kandang = kandang
    def rawat_semua_hewan(self):
        for hewan in self.kandang.get_semua_hewan():
            hewan.makan()
            if isinstance(hewan, BisaTerbang):
                hewan.terbang()
            if isinstance(hewan, BisaBerenang):
                hewan.berenang()
```

---

## Cara Menjalankan

```bash
# Clone repository
git clone https://github.com/fajriyahyulia/KelasB_Kelompok4_SOLID.git
cd KelasB_Kelompok4_SOLID

# Jalankan kode awal
python kode_awal.py

# Jalankan salah satu solusi
python solusi/solusi_srp.py
```

---

## Referensi

- Yuana, R. A. (2025). *SOLID Principles: Konsep Single Responsibility dalam Koding*. Rosihan Ari's Blog. https://blog.rosihanari.net/solid-principles-pentingnya-single-responsibility-principle-dalam-koding/
- Yuana, R. A. (2025). *SOLID Principles: Memahami Open-Closed Principle*. Rosihan Ari's Blog. https://blog.rosihanari.net/solid-principles-memahami-open-closed-principle-ocp/
- Yuana, R. A. (2025). *SOLID Principles: Pentingnya Prinsip Liskov Substitution*. Rosihan Ari's Blog. https://blog.rosihanari.net/solid-principles-memahami-prinsip-liskov-substitution/
- Yuana, R. A. (2025). *SOLID Principles: Pentingnya Prinsip Interface Segregation dalam Coding*. Rosihan Ari's Blog. https://blog.rosihanari.net/solid-principles-apa-itu-interface-segregation-principle/
- Yuana, R. A. (2025). *SOLID Principles: Dependency Inversion Principle dalam Pemrograman*. Rosihan Ari's Blog. https://blog.rosihanari.net/konsep-solid-dependency-inversion-principle-dalam-pemrograman/
- Python Software Foundation. (2024). *abc — Abstract Base Classes*. https://docs.python.org/3/library/abc.html

---

<div align="center">
  <sub>Kelompok 4 — Kelas B | Pendidikan Teknik Informatika dan Komputer | 2025/2026</sub>
</div>

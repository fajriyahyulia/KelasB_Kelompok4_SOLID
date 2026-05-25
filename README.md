# 🐾 Kelas B — Kelompok 4 | Analisis Prinsip SOLID

> Tugas Mata Kuliah Pemrograman Berorientasi Projek 
> Program Studi Pendidikan Teknik Informatika dan Komputer

---

## 👥 Anggota Kelompok

| NIM | Nama | Bagian |
|---|---|---|
| K3525005 | Fajriyah Yulia Az Zahra | Ketua & Koordinator |
| K3525006 | Fatimah Az Zahra | Single Responsibility Principle (SRP) |
| K3525039 | Riska Nur Rahmawati | Open/Closed Principle (OCP) |
| K3525042 | Vincensius Vicko Riska Saputra | Liskov Substitution Principle (LSP) |
| K3525043 | Wijang Pratama Putra | Interface Segregation Principle (ISP) |
| K3525045 | Abid Satriyo Maulana | Dependency Inversion Principle (DIP) |

---

## 📌 Deskripsi Proyek

Repositori ini berisi hasil kerja kelompok dalam menganalisis dan menerapkan
prinsip-prinsip **SOLID** pada studi kasus program manajemen **Kebun Binatang**
berbasis Python.

---

## 📁 Struktur Direktori
📦 repository
├── 📄 kode_awal.py       → Kode program sebelum perbaikan
├── 📄 analisis.md        → Penjelasan lengkap analisis & solusi
└── 📁 solusi/
├── srp.py           → Solusi Single Responsibility Principle
├── ocp.py           → Solusi Open/Closed Principle
├── lsp.py           → Solusi Liskov Substitution Principle
├── isp.py           → Solusi Interface Segregation Principle
└── dip.py           → Solusi Dependency Inversion Principle

---

## 🔍 Jawaban Analisis (Soal 1 & 2)

### 1. Apakah kode sudah memenuhi semua prinsip SOLID?

**Belum.** Kode tersebut masih melanggar sebagian besar prinsip SOLID,
terutama dalam hal pewarisan, antarmuka, dan ketergantungan antar *class*.

---

### 2. Prinsip mana yang terpenuhi dan yang dilanggar?

#### ⚠️ S — Single Responsibility Principle *(Sebagian Terpenuhi)*

Pemisahan *class* secara umum sudah memiliki tujuan masing-masing —
`Hewan` untuk data hewan, `Kandang` untuk penyimpanan, `KebunBinatang`
untuk manajemen operasional. Namun, method `terbang()` di dalam class
`Hewan` merupakan tanggung jawab yang tidak relevan untuk semua hewan,
sehingga prinsip ini belum sepenuhnya terpenuhi.

#### ❌ O — Open/Closed Principle *(Dilanggar)*

Jika ingin menambahkan perilaku baru (misalnya hewan yang bisa berenang),
kita harus memodifikasi langsung method `rawat_semua_hewan()` di class
`KebunBinatang`. Sistem belum tertutup untuk modifikasi.

#### ❌ L — Liskov Substitution Principle *(Dilanggar)*

Method `rawat_semua_hewan()` memaksa **semua** hewan memanggil `terbang()`.
Jika memasukkan Harimau atau Kura-kura ke dalam `hewan_list`, mereka akan
dipaksa "terbang" — yang secara logika sangat keliru.

#### ❌ I — Interface Segregation Principle *(Dilanggar)*

Class `Hewan` memiliki method `terbang()` yang memaksa setiap hewan
bergantung pada method yang tidak mereka butuhkan. Perilaku seperti
`terbang()` seharusnya dipisah ke dalam class tersendiri (misalnya
`BisaTerbang`).

#### ❌ D — Dependency Inversion Principle *(Dilanggar)*

Class `KebunBinatang` bergantung langsung pada class konkret `Kandang`
melalui `self.kandang = Kandang()` (*tight coupling*). Seharusnya
bergantung pada abstraksi seperti interface `PenyimpananHewan`, sehingga
jenis kandang bisa diganti tanpa mengubah kode `KebunBinatang`.

---

## ✅ Ringkasan Status Prinsip SOLID

| Prinsip | Status | Keterangan Singkat |
|---|---|---|
| S — SRP | ⚠️ Sebagian | `terbang()` tidak relevan untuk semua hewan |
| O — OCP | ❌ Dilanggar | Harus modifikasi kode lama saat ada fitur baru |
| L — LSP | ❌ Dilanggar | Subclass tidak bisa menggantikan parent secara logis |
| I — ISP | ❌ Dilanggar | Semua hewan dipaksa punya method `terbang()` |
| D — DIP | ❌ Dilanggar | `KebunBinatang` bergantung pada class konkret |

---

## 💡 Solusi

Refactoring lengkap tersedia di folder `solusi/`. Pendekatan perbaikan
menggunakan **Abstract Base Class (ABC)** dari Python untuk mendefinisikan
abstraksi, memisahkan kemampuan hewan ke interface tersendiri, dan
menerapkan **Dependency Injection**.

---

*Kelompok 4 — Kelas B | 2025/2026*

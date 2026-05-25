# Tugas Kelompok: Analisis Prinsip SOLID
# Kelas B_Kelompok 4_SOLID
Tugas Analisis Prinsip SOLID

Nama Anggota Kelompok:
- Fajriyah Yulia Az Zahra K3525005 (Ketua)
- Fatimah Az Zahra K3525006 (SRP)
- Riska Nur Rahmawati K3525039 (OCP)
- Vincensius Vicko Riska Saputra K3525042 (LSP)
- Wijang Pratama Putra K3525043 (ISP)
- Abid Satriyo Maulana K3525045 (DIP)
  
Repositori ini berisi hasil kerja kelompok kami dalam menganalisis dan menerapkan prinsip-prinsip SOLID pada studi kasus program manajemen Kebun Binatang berbasis Python.

## Jawaban Analisis Kode Awal (Soal 1 & 2)

Berdasarkan analisis terhadap `kode_awal.py`, berikut adalah jawaban untuk pertanyaan 1 dan 2:

### 1. Apakah kode program di atas sudah memenuhi semua prinsip SOLID?
**Jawaban:** **Belum.** Kode tersebut masih melanggar sebagian besar prinsip SOLID, terutama dalam hal pewarisan, antarmuka, dan ketergantungan antar *class*.

### 2. Prinsip SOLID mana saja yang sudah terpenuhi dan mana yang dilanggar?

* **Single Responsibility Principle (SRP) - (Sebagian Terpenuhi / Perlu Perbaikan)**
    * **Analisis:** Pemisahan *class* secara umum sudah memiliki tujuan masing-masing (`Hewan` untuk data hewan, `Kandang` untuk tempat penyimpanan, `KebunBinatang` untuk manajemen operasional). Namun, *method* `bersihkan_kandang()` dan manajemen *list* hewan di dalam `Kandang` bisa dianggap sebagai dua tanggung jawab yang berbeda jika sistem semakin kompleks.
* **Open/Closed Principle (OCP) - (Dilanggar)**
    * **Analisis:** Jika kita ingin menambahkan perilaku baru (misalnya hewan yang bisa berenang atau berlari cepat), kita harus memodifikasi class yang sudah ada atau mengubah fungsi `rawat_semua_hewan` di `KebunBinatang`. Sistem ini belum tertutup untuk modifikasi meskipun terbuka untuk perluasan.
* **Liskov Substitution Principle (LSP) - (Dilanggar)**
    * **Analisis:** Pada *method* `rawat_semua_hewan()` di *class* `KebunBinatang`, terdapat perulangan yang memaksa semua objek hewan untuk memanggil *method* `terbang()`. Jika kita memasukkan hewan seperti Harimau atau Kura-kura ke dalam `hewan_list`, mereka akan dipaksa "terbang", yang mana secara logika dan sifat objek sangat keliru.
* **Interface Segregation Principle (ISP) - (Dilanggar)**
    * **Analisis:** *Class* dasar `Hewan` memiliki *method* `terbang()`. Ini memaksa setiap objek hewan yang diinstansiasi (bahkan yang tidak bisa terbang) untuk bergantung pada *method* yang tidak mereka butuhkan. Seharusnya perilaku seperti `terbang()` dipisah ke dalam *interface* atau *class* tersendiri (misalnya `BisaTerbang`).
* **Dependency Inversion Principle (DIP) - (Dilanggar)**
    * **Analisis:** *Class* tingkat tinggi (`KebunBinatang`) sangat bergantung pada *class* tingkat rendah yang konkret (`Kandang`). Hal ini terlihat dari kode `self.kandang = Kandang()` di dalam *constructor* (keterikatan yang kuat / *tight coupling*). Seharusnya `KebunBinatang` bergantung pada sebuah abstraksi (misalnya *interface* `PenyimpananHewan`), sehingga kita bisa mengganti jenis kandang tanpa mengubah kode di `KebunBinatang`.

---

**Struktur Direktori Proyek Ini:**
* `kode_awal.py`: Berisi kode program sebelum perbaikan.
* `solusi/`: Direktori berisi pemecahan masalah (refactoring) kode untuk setiap prinsip SOLID.
* `analisis.md`: Berisi penjelasan lengkap mengenai perbaikan kode dan implementasi solusi.

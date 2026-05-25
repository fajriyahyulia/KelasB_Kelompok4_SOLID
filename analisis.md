# Analisis Lengkap Solusi Penerapan Prinsip SOLID

File ini berisi penjelasan detail mengenai langkah-langkah *refactoring* (perbaikan kode) yang telah kami lakukan pada kode awal agar mematuhi kelima prinsip SOLID. Setiap penjelasan merujuk pada file kode Python yang ada di dalam direktori `solusi/`.

## 1. Single Responsibility Principle (SRP)
**File Solusi:** `solusi/solusi_srp.py`

**Penjelasan Perbaikan:**
Pada kode awal, *class* memiliki tanggung jawab yang sedikit tercampur. Untuk mematuhi SRP, kami memastikan setiap *class* hanya memiliki satu alasan untuk berubah (satu tanggung jawab).
* `Hewan`: Hanya bertanggung jawab menyimpan data dan *behavior* dasar hewan.
* `Kandang`: Hanya bertanggung jawab untuk manajemen penyimpanan hewan.
* `PetugasKebersihan` (Opsional/Tambahan): Kami memisahkan fungsi `bersihkan_kandang()` dari *class* `Kandang` ke *class* tersendiri khusus petugas, karena kebersihan adalah tanggung jawab entitas yang berbeda dari tempat penyimpanannya.

## 2. Open/Closed Principle (OCP)
**File Solusi:** `solusi/solusi_ocp.py`

**Penjelasan Perbaikan:**
Agar kode tertutup untuk modifikasi namun terbuka untuk perluasan (ekstensi), kami menggunakan teknik *Polymorphism*. Kami membuat *method* umum seperti `beraktivitas()` pada *class* dasar `Hewan`. Ketika ada hewan baru (misal: Ikan yang berenang, atau Burung yang terbang), kita hanya perlu membuat *class* turunan baru dan melakukan *override* pada *method* tersebut, tanpa perlu memodifikasi *method* `rawat_semua_hewan()` di *class* `KebunBinatang`.

## 3. Liskov Substitution Principle (LSP)
**File Solusi:** `solusi/solusi_lsp.py`

**Penjelasan Perbaikan:**
Kami memperbaiki logika perulangan di mana semua hewan dipaksa memanggil *method* `terbang()`. Sesuai prinsip LSP, *class* turunan harus bisa menggantikan *class* induknya tanpa mengacaukan program. Oleh karena itu, kami menghapus pemanggilan fungsi yang tidak relevan untuk semua hewan. Hewan dipanggil berdasarkan perilakunya yang spesifik melalui pengecekan tipe data atau melalui struktur *interface* yang benar, sehingga Kura-kura tidak akan dipaksa untuk memanggil fungsi terbang.

## 4. Interface Segregation Principle (ISP)
**File Solusi:** `solusi/solusi_isp.py`

**Penjelasan Perbaikan:**
Kami menghilangkan *method* `terbang()` dari *class* dasar `Hewan` karena tidak semua hewan bisa terbang. Sesuai prinsip ISP, kami memecahnya menjadi *interface* atau *class* *MixIn* yang lebih kecil dan spesifik. Contohnya, kami membuat *class* `KemampuanTerbang` dan `KemampuanBerenang`. Sebuah *class* `Burung` akan mewarisi `Hewan` dan `KemampuanTerbang`, sementara `Kucing` hanya mewarisi `Hewan`. Ini mencegah *class* bergantung pada *method* yang tidak mereka butuhkan.

## 5. Dependency Inversion Principle (DIP)
**File Solusi:** `solusi/solusi_dip.py`

**Penjelasan Perbaikan:**
Pada kode awal, `KebunBinatang` langsung menginstansiasi objek `Kandang` di dalam konstruktornya (*tight coupling*). Untuk mematuhi DIP, kami membuat abstraksi untuk penyimpan hewan (misal *class* abstrak `FasilitasPenyimpanan`). `KebunBinatang` kini menerima objek kandang melalui *Dependency Injection* (dimasukkan lewat parameter `__init__`). Dengan cara ini, `KebunBinatang` (modul tingkat tinggi) bergantung pada abstraksi, bukan pada detail konkrit (modul tingkat rendah), sehingga jika besok ada jenis "Akuarium" atau "KandangTerbuka", kita bisa memasukkannya tanpa mengubah *class* `KebunBinatang`.

---
**Kesimpulan**
Dengan menerapkan kelima prinsip SOLID di atas, kode sistem Kebun Binatang kelompok kami kini menjadi lebih modular, mudah di-*maintenance*, mudah diuji (*testable*), dan sangat fleksibel jika ingin ditambahkan fitur baru di masa depan.

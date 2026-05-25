# Analisis Penerapan Single Responsibility Principle (SRP)

**File Rujukan:** `solusi/solusi_srp.py`

---

## 1. Pengertian Singkat SRP
**Single Responsibility Principle (SRP)** menyatakan bahwa setiap kelas harus memiliki satu tanggung jawab utama. Artinya, sebuah kelas hanya boleh memiliki satu alasan untuk berubah. Jika sebuah kelas memiliki lebih dari satu tanggung jawab, maka kode tersebut akan sulit untuk dikelola dan dipelihara.

---

## 2. Analisis Masalah pada Kode Awal
Pada file `kode_awal.py`, pelanggaran prinsip SRP terjadi secara spesifik pada *class* `Kandang`:

```python
class Kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

    def bersihkan_kandang(self): # <- Pelanggaran SRP
        print("Kandang dibersihkan.")
```

### Alasan Pelanggaran:
*Class* `Kandang` di atas mengemban dua tanggung jawab yang berbeda:
* **Manajemen Data/Penyimpanan:** Bertanggung jawab menyimpan dan menambah objek hewan ke dalam *list*.
* **Operasional Perawatan:** Bertanggung jawab atas aksi atau logika membersihkan kandang sendiri.

### Dampak Pelanggaran:
> **Peringatan:** Jika di masa depan mekanisme penyimpanan hewan berubah (misalnya menggunakan *database* alih-alih *list*), *class* ini harus diubah. Begitu juga jika prosedur kebersihan berubah (misalnya membutuhkan input alat kebersihan atau parameter disinfektan), *class* ini juga harus ikut dimodifikasi. 
>
> Memiliki lebih dari satu alasan untuk berubah adalah tanda yang jelas bahwa kode ini telah melanggar **Single Responsibility Principle (SRP)**.

---

## 3. Solusi dan Refactoring Kode

Untuk memperbaiki pelanggaran ini, kami melakukan ekstraksi tanggung jawab operasional (kebersihan) ke dalam *class* baru yang berdiri sendiri.

### Langkah Perbaikan:
1. **Menghapus *method* `bersihkan_kandang()` dari *class* `Kandang`** Kini *class* `Kandang` murni berfungsi hanya sebagai tempat atau struktur data penyimpan objek hewan.
2. **Membuat *class* baru bernama `PetugasKebersihan`** Tugas satu-satunya dari *class* baru ini adalah menangani dan mengelola seluruh logika kebersihan fasilitas.
3. **Mendelegasikan Operasional Kebersihan** Di dalam *class* `KebunBinatang`, operasional kebersihan kini tidak lagi dilakukan oleh kandang itu sendiri, melainkan didelegasikan langsung kepada objek dari `PetugasKebersihan`.
```python
class Kandang:
    """Tanggung Jawab 1: Manajemen penyimpanan hewan"""
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

class PetugasKebersihan:
    """Tanggung Jawab 2: Operasional pembersihan"""
    def bersihkan_kandang(self, kandang):
        print("Petugas Kebersihan: Kandang telah dibersihkan.")
```

---

## 4. Kesimpulan

Dengan memisahkan tanggung jawab tersebut, kode menjadi lebih terorganisir dan memiliki tingkat **kohesi yang tinggi (*high cohesion*)**. 

Jika sewaktu-waktu prosedur pembersihan kandang menjadi lebih kompleks (misalnya memerlukan pengecekan jadwal, sistem shift, atau penggunaan disinfektan tertentu), pemrogram hanya perlu memodifikasi *class* `PetugasKebersihan` tanpa khawatir akan merusak atau mengganggu logika penyimpanan data yang ada di dalam *class* `Kandang`.

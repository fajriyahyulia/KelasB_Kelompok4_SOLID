# solusi_srp.py
class Hewan:
  """Tanggung jawab: Menyimpan data dan perilaku dasar entitas hewan."""
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan.")

    def terbang(self):
        # Catatan: Logika "terbang" yang salah tempat ini akan diperbaiki 
        # lebih lanjut pada prinsip LSP dan ISP. 
        # Pada file ini kita berfokus pada pemisahan tanggung jawab SRP.
        print(f"{self.nama} sedang terbang.")


class Kandang:
    """Tanggung jawab: Hanya sebagai struktur data penyimpan hewan."""
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)
    
    # Method bersihkan_kandang() DIHAPUS dari sini karena 
    # sebuah tempat/benda mati tidak membersihkan dirinya sendiri.


class PetugasKebersihan:
    """Tanggung jawab: Mengelola kebersihan fasilitas kebun binatang."""
    def bersihkan_kandang(self, kandang):
        # Menerima objek kandang dan membersihkannya
        print("Petugas Kebersihan: Kandang telah dibersihkan.")


class KebunBinatang:
    """Tanggung jawab: Mengelola alur/operasional utama fasilitas."""
    def __init__(self):
        self.kandang = Kandang()
        self.petugas = PetugasKebersihan()

    def rawat_semua_hewan(self):
        print("--- Memulai Perawatan Hewan ---")
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            hewan.terbang()
        
        # Tanggung jawab kebersihan kini diserahkan ke class ahlinya
        self.petugas.bersihkan_kandang(self.kandang)


# ==========================================
# Contoh Penggunaan Kode:
# ==========================================
if __name__ == "__main__":
    burung = Hewan("Burung Beo", "Burung")
    
    kebun_binatang = KebunBinatang()
    kebun_binatang.kandang.tambah_hewan(burung)
    
    kebun_binatang.rawat_semua_hewan()

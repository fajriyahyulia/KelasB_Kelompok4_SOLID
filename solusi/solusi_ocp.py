from abc import ABC, abstractmethod
# ============================================================
# SOLUSI OCP - Open-Closed Principle [oleh Riska Nur Rahmawati]
# ============================================================
# Terbuka untuk EKSTENSI (tambah class baru)
# Tertutup untuk MODIFIKASI (tidak ubah class lama)

class Hewan(ABC):
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    @abstractmethod
    def makan(self):
        pass
    @abstractmethod
    def aktivitas(self):
        pass
      
# Ekstensi 1: Hewan Darat
class HewanDarat(Hewan):
    def makan(self):
        print(f"{self.nama} sedang makan.")

    def aktivitas(self):
        print(f"{self.nama} sedang berlari.")
      
# Ekstensi 2: Hewan Terbang
class HewanTerbang(Hewan):
    def makan(self):
        print(f"{self.nama} sedang makan.")
    def aktivitas(self):
        print(f"{self.nama} sedang terbang.")

# Ekstensi 3: Hewan Air
# Tambah hewan baru TANPA ubah class yang sudah ada
class HewanAir(Hewan):
    def makan(self):
        print(f"{self.nama} sedang makan.")
    def aktivitas(self):
        print(f"{self.nama} sedang berenang.")

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
    # Method ini TIDAK perlu diubah walau ada hewan baru
    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            hewan.aktivitas()

print("=" * 50)
print("UJI COBA SOLUSI OCP")
print("=" * 50)

kebun = KebunBinatang()
kebun.kandang.tambah_hewan(HewanDarat("Singa", "Darat"))
kebun.kandang.tambah_hewan(HewanTerbang("Elang", "Udara"))
kebun.kandang.tambah_hewan(HewanAir("Lumba-lumba", "Air"))
kebun.rawat_semua_hewan()
kebun.kandang.bersihkan_kandang()

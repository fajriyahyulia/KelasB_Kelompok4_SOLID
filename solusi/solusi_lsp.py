# Vincensius Vicko (K3525042)
# Solusi LSP
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    def makan(self):
        print(f"{self.nama} sedang makan.")
# Perilaku spesifik dibuat ke dalam class turunan khusus
class HewanTerbang(Hewan):
    def terbang(self):
        print(f"{self.nama} sedang terbang.")
class HewanBerenang(Hewan):
    def berenang(self):
        print(f"{self.nama} sedang berenang.")
# Contoh Hewan yg tidak bisa terbang
class Kucing(Hewan):
    pass # Kucing hanya mewarisi makan()
# Contoh Hewan yg bisa terbang
class BurungElang(HewanTerbang):
    pass # Elang mewarisi makan() dan terbang()
class Kandang:
    def __init__(self):
        self.hewan_list = []
    def tambah_hewan(self, hewan: Hewan):
        self.hewan_list.append(hewan)
    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")
class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang()
    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            # Semua hewan pasti bisa makan (Memenuhi LSP)
            hewan.makan()
            # Pengecekan tipe untuk memanggil metode spesifik 
            if isinstance(hewan, HewanTerbang):
                hewan.terbang()
            elif isinstance(hewan, HewanBerenang):
                hewan.berenang()

if __name__ == "__main__":
    kebun = KebunBinatang()
    
    kucing = Kucing("Momo", "Mamalia")
    elang = BurungElang("Garuda", "Burung")
    
    kebun.kandang.tambah_hewan(kucing)
    kebun.kandang.tambah_hewan(elang)
    
    kebun.rawat_semua_hewan()

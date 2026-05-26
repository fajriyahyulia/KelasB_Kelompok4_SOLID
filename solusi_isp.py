from abc import ABC, abstractmethod

class Hewan(ABC):
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    @abstractmethod
    def makan(self):
        pass

class BisaTerbang(ABC):
    @abstractmethod
    def terbang(self):
        pass

class Burung(Hewan, BisaTerbang):
    def makan(self):
        print(f"Burung {self.nama} sedang makan biji-bijian.")

    def terbang(self):
        print(f"Burung {self.nama} sedang terbang di langit.")

class Singa(Hewan):
    def makan(self):
        print(f"Singa {self.nama} sedang makan daging.")

class Kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan: Hewan):
        self.hewan_list.append(hewan)

    def bersihkan_kandang(self):
        print("Kandang telah dibersihkan.")

class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang()

    def rawat_semua_hewan(self):
        print("--- Memulai Perawatan Hewan ---")
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            if isinstance(hewan, BisaTerbang):
                hewan.terbang()
            else:
                print(f"{hewan.nama} tidak bisa terbang.")
            print("-" * 30)

if __name__ == "__main__":
    zoo = KebunBinatang()
    
    burung_kakaktua = Burung("Beo", "Unggas")
    singa_afrika = Singa("Simba", "Mamalia")
    
    zoo.kandang.tambah_hewan(burung_kakaktua)
    zoo.kandang.tambah_hewan(singa_afrika)
    
    zoo.rawat_semua_hewan()
# Solusi ISP - Interface Segregation Principle
# Interface dipecah kecil-kecil sesuai kemampuan hewan

from abc import ABC, abstractmethod

# Interface kecil dan spesifik
class KemampuanMakan(ABC):
    @abstractmethod
    def makan(self):
        pass

class KemampuanTerbang(ABC):
    @abstractmethod
    def terbang(self):
        pass

class KemampuanBerenang(ABC):
    @abstractmethod
    def berenang(self):
        pass

# Setiap hewan hanya mewarisi kemampuan yang dimilikinya
class Burung(KemampuanMakan, KemampuanTerbang):
    def __init__(self, nama):
        self.nama = nama
    def makan(self):
        print(f"{self.nama} sedang makan.")
    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class Ikan(KemampuanMakan, KemampuanBerenang):
    def __init__(self, nama):
        self.nama = nama
    def makan(self):
        print(f"{self.nama} sedang makan.")
    def berenang(self):
        print(f"{self.nama} sedang berenang.")

class Kucing(KemampuanMakan):
    def __init__(self, nama):
        self.nama = nama
    def makan(self):
        print(f"{self.nama} sedang makan.")

class Bebek(KemampuanMakan, KemampuanTerbang, KemampuanBerenang):
    def __init__(self, nama):
        self.nama = nama
    def makan(self):
        print(f"{self.nama} sedang makan.")
    def terbang(self):
        print(f"{self.nama} sedang terbang rendah.")
    def berenang(self):
        print(f"{self.nama} sedang berenang.")

if __name__ == "__main__":
    hewan_list = [
        Burung("Elang"),
        Ikan("Nemo"),
        Kucing("Momo"),
        Bebek("Donald"),
    ]

    print("--- Semua hewan makan ---")
    for h in hewan_list:
        h.makan()

    print("\n--- Hewan yang bisa terbang ---")
    for h in hewan_list:
        if isinstance(h, KemampuanTerbang):
            h.terbang()

    print("\n--- Hewan yang bisa berenang ---")
    for h in hewan_list:
        if isinstance(h, KemampuanBerenang):
            h.berenang()

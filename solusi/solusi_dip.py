# Abid Satriyo (K3525045)
# Solusi DIP

from abc import ABC, abstractmethod

# Interface untuk kandang
class IKandang(ABC):

    @abstractmethod
    def tambah_hewan(self, hewan):
        pass

    @abstractmethod
    def ambil_semua_hewan(self):
        pass

    @abstractmethod
    def bersihkan(self):
        pass


# Implementasi kandang
class Kandang(IKandang):

    def __init__(self):
        self._hewan_list = []

    def tambah_hewan(self, hewan):
        self._hewan_list.append(hewan)

    def ambil_semua_hewan(self):
        return self._hewan_list

    def bersihkan(self):
        print("Kandang dibersihkan.")


# Class hewan
class Hewan:

    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"{self.nama} sedang makan.")


# KebunBinatang bergantung pada abstraksi (IKandang)
class KebunBinatang:

    def __init__(self, kandang: IKandang):
        self.kandang = kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.ambil_semua_hewan():
            hewan.makan()


# Program utama
kandang = Kandang()

hewan1 = Hewan("Singa")
hewan2 = Hewan("Burung")

kandang.tambah_hewan(hewan1)
kandang.tambah_hewan(hewan2)

kebun_binatang = KebunBinatang(kandang)
kebun_binatang.rawat_semua_hewan()

kandang.bersihkan()

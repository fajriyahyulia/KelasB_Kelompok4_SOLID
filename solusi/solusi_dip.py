from abc import ABC, abstractmethod

class IKandang(ABC):
    @abstractmethod
    def tambah_hewan(self, hewan):
        pass

    @abstractmethod
    def ambil_semua_hewan(self):
        passhttps://github.com/fajriyahyulia/KelasB_Kelompok4_SOLID/projects

    @abstractmethod
    def bersihkan(self):
        pass

class Kandang(IKandang):
    def __init__(self):
        self._hewan_list = []

    def tambah_hewan(self, hewan):
        self._hewan_list.append(hewan)

    def ambil_semua_hewan(self):
        return self._hewan_list

    def bersihkan(self):
        print("Kandang dibersihkan.")

class KebunBinatang:
    def __init__(self, kandang: IKandang):
        self.kandang = kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.ambil_semua_hewan():
            hewan.makan()

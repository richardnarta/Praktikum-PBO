#Richard / 121140035

import random

class mahasiswa:
    def __init__(self, nama, nim, kelas, sks):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.sks = sks
    
    def __gacha(): 
        return random.randint(50,100)
    
    def gacha_nilai(self):
        print(f"\ngacha nilai fisika mahasiswa  : {mahasiswa.__gacha()}")
        print(f"gacha nilai biologi mahasiswa : {mahasiswa.__gacha()}")
    
    def cetak_data(self):
        print(f"Nama mahasiswa  : {self.nama}")
        print(f"NIM mahasiswa   : {self.nim}")
        print(f"kelas mahasiswa : {self.kelas}")
        print(f"sks mahasiswa   : {self.sks}")
        
mahasiswa1 = mahasiswa("Richard","121140035","RB","23")
mahasiswa1.cetak_data()
mahasiswa1.gacha_nilai()
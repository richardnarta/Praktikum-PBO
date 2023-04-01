"""
Yamako merupakan sebuah perusahaan Robot yang memiliki 3 tipe robot turunan utama
yaitu Antares, Alphasetia, dan Lecalicus. Dimana ketiga robot tersebut mempunyai
karakteristik yang berbeda-beda dengan detail seperti tabel di bawah:
---
Bantulah perusahaan Yamako untuk menentukan robot terkuat yang dimilikinya dengan
menyusun permainan gunting-batu-kertas serta pemain berupa para robot. Apabila
suatu robot menang gunting-batu-kertas pada suatu turn, maka fungsi lakukan_aksi() pada
robot yang menang tersebut akan dieksekusi. Contoh output program (tidak mesti sama
persis, aksi lawan bisa saja diotomatisasi):

Richard / 121140035
"""

import random

class Robot:
    jumlah_turn = 1
    
    def __init__(self, nama, health, damage):
        self.nama = nama
        self.health = health
        self.damage = damage
        
    def lakukan_aksi(self, lawan):
        lawan.health -= self.damage
        if(lawan.health < 0):
            lawan.health = 0
        print(f"Robotmu ({self.nama}) menyerang sebanyak {int(self.damage)} DMG")
        self.jumlah_turn += 1
        lawan.jumlah_turn += 1
    
    def terima_aksi(self, lawan):
        self.health -= lawan.damage
        if(self.health < 0):
            self.health = 0
        print(f"Robot lawan ({lawan.nama}) menyerang sebanyak {int(lawan.damage)} DMG")
        self.jumlah_turn += 1
        lawan.jumlah_turn += 1
    
    def buff(self):
        pass
    
class Antares(Robot):
    def __init__(self):
        super().__init__('Antares',  50_000, 5_000)
    
    def buff(self):
        if (self.jumlah_turn %3 == 0):
            self.damage *= 1.5
            return True
        
    def base(self):
        self.damage /= 1.5
        
class Alphasetia(Robot) :
    def __init__(self):
        super().__init__('Alphasetia', 40_000, 6_000)       
        
    def buff(self):
        if (self.jumlah_turn %2 == 0):
            self.health += 4_000
        
class Lecalicus(Robot):
    def __init__(self):
        super().__init__('Lecalicus', 45_000, 5_500)
        
    def buff(self):
        if (self.jumlah_turn %4 == 0):
            self.health += 7_000
            self.damage *= 2
            return True
    
    def base(self):
        self.damage /= 2

def create_robot(opsi):
    if(opsi == 1):
        return Antares()
    elif(opsi == 2):
        return Alphasetia()
    elif(opsi == 3):
        return Lecalicus()
    
def gunting_batu_kertas(opsi_saya, opsi_lawan):
    if(opsi_saya == 1 and opsi_lawan == 2):
        return False
    elif(opsi_saya == 2 and opsi_lawan == 3):
        return False
    elif(opsi_saya == 3 and opsi_lawan == 1):
        return False
    elif(opsi_saya == 2 and opsi_lawan == 1):
        return True
    elif(opsi_saya == 3 and opsi_lawan == 2):
        return True
    elif(opsi_saya == 1 and opsi_lawan == 3):
        return True
    elif(opsi_saya == 1 and opsi_lawan == 1):
        return "draw"
    elif(opsi_saya == 2 and opsi_lawan == 2):
        return "draw"
    elif(opsi_saya == 3 and opsi_lawan == 3):
        return "draw"

def tambah_darah(darah_sekarang, darah_sebelum_buff, status, robot):
    if(darah_sekarang != darah_sebelum_buff and status == 'saya'):
        print(f"Robotmu ({robot.nama}) menambah darah sebanyak {int(darah_sekarang-darah_sebelum_buff)} HP")
    elif(darah_sekarang != darah_sebelum_buff and status == 'lawan'):
        print(f"Robot lawan ({robot.nama}) menambah darah sebanyak {int(darah_sekarang-darah_sebelum_buff)} HP")

#-------------------------------Game Loop-------------------------------#

print("Selamat datang di pertandingan robot Yamako")

opsi_robot_saya = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
while True:
        if((opsi_robot_saya > 3 or opsi_robot_saya < 1)):
            opsi_robot_saya = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
        else:
            break
robot_saya = create_robot(opsi_robot_saya)

opsi_robot_lawan = int(input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
while True:
        if((opsi_robot_lawan > 3 or opsi_robot_lawan < 1)):
            opsi_robot_lawan = int(input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
        else:
            break
robot_lawan = create_robot(opsi_robot_lawan)

print("Selanjutnya, untuk robotmu pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting")

#-------------------Game Start-------------------#
run = True
while run:
    print(f"\nTurn saat ini: {robot_saya.jumlah_turn}")
    print(f"Robotmu ({robot_saya.nama} - {int(robot_saya.health)} HP), robot lawan ({robot_lawan.nama} - {int(robot_lawan.health)} HP)")
    
    tangan_saya = int(input(f"Pilih tangan robotmu ({robot_saya.nama}): "))
    while True:
        if((tangan_saya > 3 or tangan_saya < 1)):
            tangan_saya = int(input(f"Pilih tangan robotmu ({robot_saya.nama}): "))
        else:
            break
        
    tangan_lawan = random.randint(1,3)
    print(f"Robot lawan ({robot_lawan.nama}) memilih : {tangan_lawan}")
    
    value = gunting_batu_kertas(tangan_saya, tangan_lawan)
    if(value == True):
        darah_sebelum_buff = robot_saya.health
        
        buff = robot_saya.buff()
        tambah_darah(robot_saya.health, darah_sebelum_buff, 'saya', robot_saya)
        robot_saya.lakukan_aksi(robot_lawan)
        
        if(buff == True):
            robot_saya.base()
            
    elif(value == False):
        darah_sebelum_buff = robot_lawan.health
        
        buff = robot_lawan.buff()
        tambah_darah(robot_lawan.health, darah_sebelum_buff, 'lawan', robot_lawan)
        robot_saya.terima_aksi(robot_lawan)
        
        if(buff == True):
            robot_lawan.base()
            
    else:
        print("Turn saat ini draw...")
        robot_saya.jumlah_turn += 1
        robot_lawan.jumlah_turn += 1
    
    if(robot_lawan.health <= 0) or (robot_saya.health <= 0):
        print("\nPermainan Berakhir")
        print(f"Robotmu ({robot_saya.nama} - {int(robot_saya.health)} HP), robot lawan ({robot_lawan.nama} - {int(robot_lawan.health)} HP)")
        
        if(robot_lawan.health > robot_saya.health):
            print("\nAnda Kalah!")
        else:
            print("\nSelamat! Anda menang")
            
        run = False
    

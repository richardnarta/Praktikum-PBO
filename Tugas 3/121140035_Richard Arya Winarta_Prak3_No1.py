"""
Buatlah sebuah game Minesweeper seperti output di bawah ini, dimana data tiap-tiap kotak
(area) disimpan dalam kelas Kotak (dalam kasus di bawah, terdapat 9 kelas Kotak yang
diinstansiasi).
Kelas Kotak ini mempunyai atribut instance private berupa isi (bom/kosong), status (belum
dibuka/sudah dibuka); atribut kelas publik berupa jumlah_bom (nilainya konsisten antar
instansi tiap objek kotak); serta fungsi publik berupa tampilkan ("?" jika belum dibuka, "x"
jika bom, dan "o" jika kosong) dan buka_kotak untuk mengubah status kotak dari belum
dibuka menjadi sudah dibuka. Atribut isi kotak (bom/kosong) bersifat acak dan ditentukan
saat pertama kali kotak diinisiasi (gunakan import random bila dibutuhkan).

Richard / 121140035

"""

import random


class Kotak:
    jumlah_bom = None
    
    def __init__(self, isi, status):
        self.__isi = isi
        self.__status = status
    
    def buka_kotak(self):
        if(self.__status == "?" and self.__isi == False):
            self.__status = "o"
            return True
        elif(self.__status == "?" and self.__isi == True):
            self.__status = "x"
            return True
        else:
            print("Kotak sudah dibuka! pilih yang lain ...")
        
    def tampilkan(self):
        if(self.__status == "?"):
            print(f"? ", end = "")
        elif(self.__status == "o"):
            print(f"o ", end = "")
        elif(self.__status == "x"):
            print(f"x ", end = "")
      
    def cek_kondisi(self):
        if(self.__status == "x"):
            print("Game over! Kotak tersebut berisi bom.")
            return False
        elif(self.__status == "o"):
            print("Selamat! Kotak tersebut tidak berisi bom.")
            return True
            
    def kondisi_menang(self, kotak_kotak):
        count = 0
        for i in range(len(kotak_kotak)):
            if(kotak_kotak[i].__status == "o"):
                count += 1
        
        if(count == len(kotak_kotak)-jumlah_bom):
            print("\nSelamat! Anda telah memenangkan game.")
            print("Anda berhasil menghindari semua bom.\n")
            return False

def display(dimensi, kotak_kotak):
    print()
    for i in range(jumlah_kotak):
        kotak_kotak[i].tampilkan()
        if(i%dimensi == dimensi-1):
            print()

   
kotak = []
global jumlah_kotak


# -------------------start game-------------------
print("Permainan Minesweeper")
dimensi = int(input("Masukkan dimensi area: "))
jumlah_kotak= dimensi*dimensi
while True:  
    jumlah_bom = int(input("Masukkan jumlah bom: "))
    if(jumlah_bom < (jumlah_kotak) and jumlah_bom > 0):
        break
Kotak.jumlah_bom = jumlah_bom

# ------------penentuan lokasi bom----------------
lokasi_bom = []

for i in range(jumlah_bom):
    run = True
    while run:
        x = random.randint(0, (jumlah_kotak)-1)
        if(i == 0):
            lokasi_bom.append(x)
            run = False
        else:
            for j in range(len(lokasi_bom)):
                if(x == lokasi_bom[j]):
                    break
                elif(j == (len(lokasi_bom)-1) and x!= lokasi_bom[j]):
                    lokasi_bom.append(x)
                    run = False
lokasi_bom.sort()
print(lokasi_bom)

# ------------pembuatan objek kotak----------------
kotak_kotak = []
objek_temp = None

for i in range(jumlah_kotak):
    bom = False
    for j in lokasi_bom:
        if(j == i):
            objek_temp = Kotak(True, "?")
            kotak_kotak.append(objek_temp)
            bom = True
    if(bom != True):     
        objek_temp = Kotak(False, "?")
        kotak_kotak.append(objek_temp)


# -----------------game loop----------------------
running = True
display(dimensi, kotak_kotak)
bukan_bom = jumlah_kotak - jumlah_bom

while running:
    print(f"Jumlah kotak bukan bom yang harus dibuka : {bukan_bom}")
    opsi = int(input(f"Masukkan nomor kotak yang ingin dibuka (1-{jumlah_kotak}): "))
    
    if(opsi > jumlah_kotak or opsi < 0):
        print("input invalid! Silahkan input kembali ...")
    else:
        buka = kotak_kotak[opsi-1].buka_kotak()

        display(dimensi, kotak_kotak)

        
        if (buka == True):
            cek_kotak = kotak_kotak[opsi-1].cek_kondisi()

        cek_menang = kotak_kotak[opsi-1].kondisi_menang(kotak_kotak)
        bukan_bom -= 1
        if(cek_kotak == False or cek_menang == False):
            running = False
            
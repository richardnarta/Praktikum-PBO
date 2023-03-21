"""
Om Bambang memiliki sebuah toko komputer yang menjual komputer rakitannya sendiri.
Bantulah Om Bambang untuk membuat sebuah program sederhana dari sebuah kelas induk
Komputer dan kelas turunan Processor, RAM, HDD, VGA, dan PSU
--
Tujuan akhir program adalah menampilkan seluruh komponen yang Om Bambang
gunakan untuk masing-masing komputer yang dirakitnya. Kalian dapat memanfaatkan
sebuah list yang dapat menampung komponen komputer tersebut untuk setiap komputer yang
telah dirakit oleh Om Bambang.

Richard / 121140035
"""

class Komputer:
    def __init__(self, nama, jenis, harga, merk):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.merk = merk
        
    def print(self):
        print(f"{self.jenis} {self.nama} produksi {self.merk}")
        
class Processor(Komputer):
    def __init__(self, nama, jenis, harga, merk, jumlah_core, kecepatan_processor):
        super().__init__(nama, jenis, harga, merk)
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor
   
class RAM(Komputer):
    def __init__(self, nama, jenis, harga, merk, capacity):
        super().__init__(nama, jenis, harga, merk)
        self.capacity = capacity
        
class HDD(Komputer):
    def __init__(self, nama, jenis, harga, merk, capacity, rpm):
        super().__init__(nama, jenis, harga, merk) 
        self.capacity = capacity
        self.rpm = rpm
        
class VGA(Komputer):
    def __init__(self, nama, jenis, harga, merk, capacity):
        super().__init__(nama, jenis, harga, merk)
        self.capacity = capacity

class PSU(Komputer):
    def __init__(self, nama, jenis, harga, merk, daya):
        super().__init__(nama, jenis, harga, merk)
        self.daya = daya

p1 = Processor('Core i7 7740X', 'Processor', 4350000, 'Intel', 4, '4.3GHz')
p2 = Processor('Ryzen 5 3600', 'Processor', 250000, 'AMD', 4, '4.3GHz')
ram1 = RAM('DDR4 SODimm PC19200/2400MHz','RAM', 328000, 'V-Gen','4GB')
ram2 = RAM('DDR4 2400MHz','RAM', 328000, 'G.SKILL','4GB')
hdd1 = HDD('HDD 2.5 inch', 'HDD', 295000, 'Seagate', '500GB', 7200)
hdd2 = HDD('HDD 2.5 inch', 'HDD', 295000, 'Seagate', '1000GB', 7200)
vga1 = VGA('GTX 1050', 'VGA', 250000, 'Asus', '2GB')
vga2 = VGA('1060Ti', 'VGA', 250000, 'Asus', '8GB')  
psu1 = PSU('Corsair V550', 'PSU', 250000, 'Corsair', '500W')
psu2 = PSU('Corsair V550', 'PSU', 250000, 'Corsair', '500W')

rakit = [[p1,ram1,hdd1,vga1,psu1],[p2,ram2,hdd2,vga2,psu2]]

x = 1
for i in rakit:
    print(f"Komputer {x}")
    for j in i:
        j.print()
    print()
    x += 1

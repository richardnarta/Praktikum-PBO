from abc import *
from datetime import *

"""
Buatlah sebuah kelas abstrak yaitu AkunBank, dimana pada kelas abstrak ini terdapat
beberapa atribut berupa nama, tahun_daftar, dan saldo pelanggan; serta fungsi
konkret berupa lihat_saldo. Pada kelas abstrak tersebut, juga terdapat fungsi abstrak
yang akan diturunkan ke kelas turunannya yaitu transfer saldo dan lihat suku bunga
(interest). Adapun kelas turunan dari AkunBank dan implementasinya adalah sebagai
berikut:

Richard / 121140035
"""

class AkunBank:
    def __init__(self, nama, tahun_daftar, saldo):
        self.nama = nama
        self.tahun_daftar = tahun_daftar
        self.saldo = saldo
        
        temp = datetime.now()
        self.umur = int(temp.strftime("%Y")) - self.tahun_daftar
        
    # method konkrit
    def lihat_saldo(self):
        return self.saldo
    
    @abstractmethod
    def transfer_saldo(self):
        pass
    
    @abstractmethod
    def suku_bunga(self):
        pass
    
class AkunGold(AkunBank):
    def transfer_saldo(self, transfer):
        if(self.umur >= 3 and transfer > 100_000):
            return 0
        elif(self.umur < 3 and transfer > 100_000):
            return 2_000
        elif(transfer <= 100_000):
            return 0
            
    def suku_bunga(self):
        if(self.umur >=3 and self.saldo >= 1_000_000_000):
            return 1
        elif(self.umur < 3 and self.saldo >= 1_000_000_000):
            return 2
        elif(self.saldo < 1_000_000_000):
            return 3

class AkunSilver(AkunBank):
    def transfer_saldo(self, transfer):
        if(self.umur >= 3 and transfer > 100_000):
            return 2_000
        elif(self.umur < 3 and transfer > 100_000):
            return 5_000
        elif(transfer <= 100_000):
            return 0
            
    def suku_bunga(self):
        if(self.umur >=3 and self.saldo >= 10_000_000):
            return 1
        elif(self.umur < 3 and self.saldo >= 10_000_000):
            return 2
        elif(self.saldo < 10_000_000):
            return 3
"""
Buatlah kelas AkunBank yang memiliki atribut instance berupa no_pelanggan,
nama_pelanggan, dan jumlah_saldo (bersifat private). Kelas AkunBank tersebut juga
memiliki atribut kelas berupa list_pelanggan (berisi data-data pelanggan tiap instansi). Pada
kelas AkunBank, terdapat fungsi yang dapat dieksekusi oleh pelanggan, yaitu lihat_menu(),
lihat_saldo(), tarik_tunai(), dan transfer() (implementasikan sendiri)

Richard / 121140035
"""

class AkunBank:
    list_pelanggan = []
    
    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        
        self.no = no_pelanggan
        self.nama = nama_pelanggan
        self.__saldo = jumlah_saldo
        
    def lihat_menu(self, list_pelanggan):
        
        print("Selamat datang di Bank Jago")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")
        
        opsi = input("Masukkan nomor input: ")
        print()
        
        if(opsi == "1"):
            AkunBank.lihat_saldo(self, list_pelanggan)
        elif(opsi == "2"):
            AkunBank.tarik_tunai(self, list_pelanggan)
        elif(opsi == "3"):
            AkunBank.transfer(self, list_pelanggan)
        elif(opsi == "4"):
            exit()
    
    def lihat_saldo(self, list_pelanggan):
        
        print(f"{self.nama} memiliki saldo {self.__saldo:,}\n")
        AkunBank.lihat_menu(self, list_pelanggan)
    
    def tarik_tunai(self, list_pelanggan):
        
        tarik_tunai = int(input(f"Masukkan jumlah nominal yang ingin ditarik: "))
        
        if(tarik_tunai > self.__saldo):
            print("Nominal saldo yang Anda punya tidak cukup!")    
        else:
            self.__saldo -= tarik_tunai
            print("Saldo berhasil ditarik!\n")
            
        AkunBank.lihat_menu(self, list_pelanggan)
    
    def transfer(self,list_pelanggan):
    
        transfer = int(input("Masukkan nominal yang ingin ditransfer: "))
        akun_tujuan = int(input("Masukkan no rekening tujuan: "))
        
        for i in range(len(list_pelanggan)):
            
            if(akun_tujuan == list_pelanggan[i].no and self.__saldo > transfer):
                list_pelanggan[i].__saldo += transfer
                self.__saldo -= transfer
                print(f"Transfer Rp {transfer:,} ke {list_pelanggan[i].nama} sukses!\n")
                break
            elif(akun_tujuan != list_pelanggan[i].no and i == (len(list_pelanggan))-1):
                print("No rekening tujuan tidak dikenal! Kembali ke menu utama ...\n")    
            elif(self.__saldo < transfer):
                print("Saldo tidak mencukupi! Kembali ke menu utama ...\n")
                
        AkunBank.lihat_menu(self, list_pelanggan)
        
    
Akun1 = AkunBank(1234, "Richard", 5_000_000_000)
Akun2 = AkunBank(2345, "Ukraina", 6_666_666_666)
Akun3 = AkunBank(3456, "Elon Musk", 9_999_999_999)

AkunBank.list_pelanggan = [Akun1, Akun2, Akun3]
AkunBank.list_pelanggan[0].lihat_menu(AkunBank.list_pelanggan)

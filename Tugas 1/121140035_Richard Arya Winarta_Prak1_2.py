"""
Buatlah program yang dapat menerima inputan username dan password dari user
sebanyak 3 kali. Jika percobaan oleh user kurang dari sama dengan 3 kali maka
berhasil login, jika lebih dari 3 kali maka akun diblokir. Dengan username yang
digunakkan ialah seperti berikut:

username = informatika
password = 12345678

Richard / 121140035
"""


for i in range (3):
    username = str(input("Username anda :"))
    password = str(input("Password anda : "))
    if (username == 'informatika' and password == '12345678' and i<3):
        print("Berhasil login!")
        break
    elif(username != 'informatika' and password != '12345678' and i<2):
        print("Username atau password salah coba lagi")
    else:
        print("Anda diblokir")
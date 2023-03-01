"""
Buatlah program yang dapat menerima n input bilangan integer dari user kemudian
menghasilkan output kotak bintang dengan panjang n, dan lebar n. contoh input dan
output:

Richard / 121140035
"""

x = int(input())

for i in range(x):
    for j in range(x):
        print('*', end="")
    print()
# Import Paket

x = 15
y = 2

# Import modul dari paket
from MTK import Penjumlahan, Pengurangan, Perkalian, Pembagian, Modulus

hasil_penjumlahan = Penjumlahan.jumlah(x, y)
hasil_pengurangan = Pengurangan.kurang(x, y)
hasil_perkalian = Perkalian.kali(x, y)
hasil_pembagian = Pembagian.bagi(x, y)
hasil_modulus = Modulus.mod(x, y)

print('{} + {} = {}'.format(x, y, hasil_penjumlahan))
print('{} - {} = {}'.format(x, y, hasil_pengurangan))
print('{} * {} = {}'.format(x, y, hasil_perkalian))
print('{} / {} = {}'.format(x, y, hasil_pembagian))
print('{} % {} = {}'.format(x, y, hasil_modulus))

# Import fungsi dari modul dan paket
from MTK.Penjumlahan import jumlah

x = 15
y = 2

hasil_penjumlahan = jumlah(x, y)
print('{} + {} = {}'.format(x, y, hasil_penjumlahan))

# Import seluruh hal dari paket dan modul
from MTK.Penjumlahan import *

# Import dan menamai ulang modul dari paket 
from MTK import Perkalian as pkali

# Import dan menamai ulang fungsi dari modul dan paket
from MTK.Penjumlahan import jumlah as jum
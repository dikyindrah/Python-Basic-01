# Import modul
x = 5
y = 2

# Import seluruh hal yang ada pada modul
import Matematika

hasil_penjumlahan = Matematika.penjumlahan(x, y)
hasil_pengurangan = Matematika.pengurangan(x, y)
hasil_pembagian = Matematika.pembagian(x, y)
hasil_perkalian = Matematika.perkalian(x, y)

print('{} + {} = {}'.format(x, y, hasil_penjumlahan))
print('{} - {} = {}'.format(x, y, hasil_pengurangan))
print('{} / {} = {}'.format(x, y, hasil_pembagian))
print('{} * {} = {}'.format(x, y, hasil_perkalian))

# Import sebagian hal yang ada pada modul
from Matematika import penjumlahan, pengurangan

hasil_penjumlahan = penjumlahan(x, y)
hasil_pengurangan = pengurangan(x, y)

print('{} + {} = {}'.format(x, y, hasil_penjumlahan))
print('{} - {} = {}'.format(x, y, hasil_pengurangan))

# Import dan menamai ulang modul
import Matematika as mat

hasil_penjumlahan = mat.penjumlahan(x, y)
print('{} + {} = {}'.format(x, y, hasil_penjumlahan))

# Import dan menamai ulang fungsi
from Matematika import penjumlahan as jumlah

hasil_penjumlahan = jumlah(x, y)
print('{} + {} = {}'.format(x, y, hasil_penjumlahan))

# Import seluruh hal yang ada didalam modul
from Matematika import *

print('list_angka = {}'.format(list_angka))


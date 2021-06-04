# Modul
import Matematika

x = 5
y = 2

hasil_penjumlahan = Matematika.penjumlahan(x, y)
hasil_pengurangan = Matematika.pengurangan(x, y)
hasil_pembagian = Matematika.pembagian(x, y)
hasil_perkalian = Matematika.perkalian(x, y)

print('{} + {} = {}'.format(x, y, hasil_penjumlahan))
print('{} - {} = {}'.format(x, y, hasil_pengurangan))
print('{} / {} = {}'.format(x, y, hasil_pembagian))
print('{} * {} = {}'.format(x, y, hasil_perkalian))

import math

n = math.pow(x, y)
hasil_perpangkatan = int(n)
print('{}^{} = {}'.format(x, y, hasil_perpangkatan))
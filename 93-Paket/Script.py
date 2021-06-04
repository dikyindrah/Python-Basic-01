# Paket

x = 15
y = 2

# Import paket
# Cara pertama
from mtk import Pengurangan, Perkalian

hasil_pengurangan = Pengurangan.kurang(x, y)
hasil_perkalian = Perkalian.kali(x, y)

print('{} - {} = {}'.format(x, y, hasil_pengurangan))
print('{} * {} = {}'.format(x, y, hasil_perkalian))

# Cara kedua
from mtk.Penjumlahan import jumlah

hasil_penjumlahan = jumlah(x, y)
print('{} + {} = {}'.format(x, y, hasil_penjumlahan))

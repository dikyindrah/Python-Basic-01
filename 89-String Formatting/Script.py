# String formatting

print('=====String Formatting=====')

print('\n==Pemformatan String Menggunakan Operator %=====')
total_harga = 15000
print('Total Harga %d' %(total_harga))

username = 'dikyindrah'
password = '%3jafKaghal'
print('username = %s dan password = %s' %(username, password))

print('\n==Pemformatan String Menggunakan Method format()=====')
nama = 'dikyindrah'
print('Selamat datang {}'.format(nama))

hari_ini = 'rabu'
besok = 'kamis'
print('hari ini adalah {hari_ini} dan besok adalah hari {besok}'.format(hari_ini=hari_ini, besok=besok))

print('\n==Pemformatan String Menggunakan Interpolasi String (f-string)=====')
nama = 'dikyindrah'
print(f'Nama saya adalah {nama}')

x = 5
y = 10
print(f'lima ditambah sepuluh adalah {x + y} dan bukan {2 * (x + y)}')

print('\n==Pemformatan String Menggunakan String Template=====')
from string import Template

# Cara pertama
print(Template('Hari ini adalah hari $hari').substitute(hari='rabu'))

# Cara kedua
buah = 'pisang'
warna = 'kuning'
tmp = Template('Buah $buah berwarna $warna')
teks = tmp.substitute(buah=buah, warna=warna)
print(teks)


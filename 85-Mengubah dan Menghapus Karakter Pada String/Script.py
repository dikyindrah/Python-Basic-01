# Mengubah dan menghapus karakter pada string

print('=====Mengubah dan Menghapus Karakter Pada String=====')
print('\n==Mengubah Karakter Pada String=====')

# Sebelum karakter di ubah
teks = 'python'
print(teks)

# Saat karakter di ubah
teks[2] = 'k'
print(teks[2])

# Menetapkan nilai string baru pada nama variabel yang sama
teks = 'anaconda'
print(teks)

print('\n==Menghapus Karakter Pada String=====')

# Sebelum karakter di hapus
teks = 'jeruk'
print(teks)

# Saat karakter di hapus
del teks[2]
print(teks)

# Menghapus karakter yang terikat dengan string
del teks
print(teks)
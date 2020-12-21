# Tipe data tidak berurut

# Set
print('\n==========Set==========\n')

# Set dapat berisi item dengan berbagai macam tipe data
# Set berisi integer
set_integer = {23 ,45 ,12 ,88}

# Set berisi float
set_float = {3.14, 5.5, 11.6}

# Set berisi string
set_string = {'moona', 'pekora', 'gintoki'}

# Set berisi boolean
set_boolean = {True, False, True, False}

# Set berisi tipe data campuran
set_campuran = {23, 'HelloWorld!', True, 3.14}

print('\nMenampilkan seluruh item pada set : \n')
print('Set berisi integer  :', set_integer)
print('Set berisi float    :', set_float)
print('Set berisi string   :', set_string)
print('Set berisi boolean  :', set_boolean)
print('Set berisi campuran :', set_campuran)

# Set berisi list
set_list = set([1, 2, 3, 4, 5])
print('\nSet berisi list:', set_list)

# list_integer = [10, 20, 30, 40, 50]
# set_list = set(list_integer)
# print('\nSet berisi list :', set_list)

# Membuat set kosong
set_kosong = set()

# Set akan otomatis menhapus item yang sama
print('\n\nSet akan otomatis menhapus item yang sama :')
print('\nItem pada set        : 1, 2, 1, 3, 3, 4, 2, 5, 1, 3, 5, 6, 9, 8')
set_integer = {1, 2, 1, 3, 3, 4, 2, 5, 1, 3, 5, 6, 9, 8}
print('Saat item di tampilkan :', set_integer)

# Menambahakan satu item pada set
print('\n\nMenambahakan satu item pada set :')
set_nama = {'diky', 'indra'}
print('\nSebelum item ditambah :',set_nama)

set_nama.add('hermawanto')
print('\nSetelah item ditambah :', set_nama)

# Menambahkan beberapa item sekaligus
print('\n\nMenambahkan beberapa item sekaligus :')
set_angka_ganjil = {3, 5, 7}
print('\nSebelum item ditambah :',set_angka_ganjil)
set_angka_ganjil.update({3, 5, 7, 13, 15, 17})
print('\nSetelah item ditambah :', set_angka_ganjil)

# Menghapus item pada set
print('\n\nMenghapus item pada set :')
# Discard
print('\nMenghapus item menggunakan discard :')
set_makanan = {'Ayam Goreng', 'Rendang', 'Opor'}
print('\nItem sebelum di hapus :', set_makanan)
# Item yang ingin di hapus ada didalam set
set_makanan.discard('Ayam Goreng')
print('\nItem setelah di hapus :', set_makanan)

# Item yang ingin di hapus tidak ada didalam set
print('\nMenghapus item yang tidak ada didalam set :')
set_makanan.discard('Pecel Lele')
print('\n', set_makanan)

# Remove
print('\n\nMenghapus item menggunakan remove :')
set_minuman = {'Es Teh', 'Kopi', 'Teh Hangat'}
print('\nItem sebelum di hapus :', set_minuman)
# Item yang ingin di hapus ada didalam set
set_minuman.remove('Kopi')
print('\nItem setelah di hapus :', set_minuman)

# # Item yang ingin di hapus tidak ada didalam set
# print('\nMenghapus item yang tidak ada didalam set :\n')
# set_minuman.remove('Air Putih')
# print('\n', set_minuman)


# Dictionary
print('\n\n==========Dictionary==========\n')

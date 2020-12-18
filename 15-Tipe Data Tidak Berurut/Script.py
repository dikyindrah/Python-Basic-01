# Tipe data tidak berurut

# Set
print('\n==========Set==========\n')

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

print('Set berisi integer  :', set_integer)
print('Set berisi float    :', set_float)
print('Set berisi string   :', set_string)
print('Set berisi boolean  :', set_boolean)
print('Set berisi campuran :', set_campuran)

# Set berisi list
set_list = set([1, 2, 3, 4, 5])
print('\nSet berisi list  :', set_list)

# list_integer = [10, 20, 30, 40, 50]
# set_list = set(list_integer)
# print('\nSet berisi list :', set_list)

# Membuat set kosong
set_kosong = set()

# Set akan otomatis menhapus item yang sama
set_integer = {1, 2, 1, 3, 3, 4, 2, 5, 1, 3, 5, 6, 9, 8}
print('\n', set_integer)

# Menambahakan satu item pada set
set_nama = {'diky', 'indra'}
set_nama.add('hermawanto')
print('\n', set_nama)

# Menambahkan beberapa item sekaligus
set_angka_ganjil = {3, 5, 7}
set_angka_ganjil.update({3, 5, 7, 13, 15, 17})
print('\n', set_angka_ganjil)

# Menghapus item pada set
# Discard
set_makanan = {'Ayam Goreng', 'Rendang', 'Opor'}
set_makanan.discard('Ayam Goreng')
print('\n', set_makanan)

set_makanan.discard('Pecel Lele')
print('\n', set_makanan)


# Remove
set_minuman = {'Es Teh', 'Kopi', 'Teh Hangat'}
set_minuman.remove('Kopi')
print('\n', set_minuman)

set_minuman.remove('Air Putih')
print('\n', set_minuman)
# Tipe data berurut

# List
print('\n==========List==========\n')

# List dapat berisi item dengan berbagai macam tipe data
list_integer = [5, 7, 3, 9, 12]
print(list_integer[3])

list_string  = ['diky', 'gintoki', 'katsura']
print(list_string[0])

list_float = [6.5, 3.2, 9.12]
print(list_float[1])

list_boolean = [True, False, False]
print(list_boolean[2])
print('')

# List dapat menyimpan item dengan tipe data yang berbeda
list_campuran = [59, 'gintoki', True]
print(list_campuran[1])
print('')

# List dapat menyimpan variabel sebagai item
nama = 'dikyindrah'
umur = 21
tinggi_badan = 147.5 
menikah = False

list_data_diri = [nama, umur, tinggi_badan, menikah]
print(list_data_diri[0])
print(list_data_diri[1])
print(list_data_diri[2])
print(list_data_diri[3])
print('')


# Item pada list nilainya dapat di ubah
list_bilangan_genap = [4, 3, 8, 12]
# Sebelum di ubah
print(list_bilangan_genap[1])
print('')

list_bilangan_genap[1] = 6
# Setelah di ubah
print(list_bilangan_genap[1])

# List dapat menyimpan list sebagai item
# List bercabang
list_mahasiswa = [
    [881, 'diky', 'Teknik Informatika'], 
    [882, 'indrah', 'Teknik Elektro'],
    [883, 'hermawan', 'Teknik Sipil']
]

print('\nNim    :', list_mahasiswa[0][0])
print('Nama   :', list_mahasiswa[0][1])
print('Prodi  :', list_mahasiswa[0][2])

print('\nNim    :', list_mahasiswa[1][0])
print('Nama   :', list_mahasiswa[1][1])
print('Prodi  :', list_mahasiswa[1][2])

print('\nNim    :', list_mahasiswa[2][0])
print('Nama   :', list_mahasiswa[2][1])
print('Prodi  :', list_mahasiswa[2][2])
print('')


# Tuple
print('\n==========Tuple==========\n')

# Tuple dapat berisi item dengan berbagai macam tipe data
tuple_integer = (12, 37, 89)
print(tuple_integer[0])

tuple_float = (12.4, 5.5, 30.5)
print(tuple_float[1])

tuple_string = ('diky','indra','heramwanto')
print(tuple_string[2])

tuple_boolean = (False, True, False, True)
print(tuple_boolean[0])
print('')

# Tuple dapat menyimpan item dengan tipe data yang berbeda
tuple_campuran = ('diky', 21, 160.5, False)
print(tuple_campuran[3])
print('')

# Tuple dapat menyimpan variabel sebagai item
nama = 'dikyindrah'
umur = 21
tinggi_badan = 147.5 
menikah = False

tuple_data_diri = (nama, umur, tinggi_badan, menikah)
print(tuple_data_diri[0])
print(tuple_data_diri[1])
print(tuple_data_diri[2])
print(tuple_data_diri[3])
print('')

# Item pada tuple nilainya tidak dapat di ubah
tuple_bilangan_ganjil = (3, 5, 7, 8)
# Sebelum di ubah
print(tuple_bilangan_ganjil[3])
print('')

# tuple_bilangan_ganjil[3] = 13
# # Setelah di ubah
# print(tuple_bilangan_ganjil[3])

# Jika kita mengubah nilai item pada tuple maka akan terjadi eror
# TypeError: 'tuple' object does not support item assignment

# Tuple dapat menyimpan tuple atau list sebagai item
# Tuple bercabang
tuple_mahasiswa = (
    (881, 'diky', 'Teknik Informatika'), 
    [882, 'indrah', 'Teknik Elektro'],
    (883, 'hermawan', 'Teknik Sipil')
)

print('\nNim    :', tuple_mahasiswa[0][0])
print('Nama   :', tuple_mahasiswa[0][1])
print('Prodi  :', tuple_mahasiswa[0][2])

print('\nNim    :', tuple_mahasiswa[1][0])
print('Nama   :', tuple_mahasiswa[1][1])
print('Prodi  :', tuple_mahasiswa[1][2])

print('\nNim    :', tuple_mahasiswa[2][0])
print('Nama   :', tuple_mahasiswa[2][1])
print('Prodi  :', tuple_mahasiswa[2][2])
print('')

# Item pada tuple tidak bisa di ubah, tetapi jika item tersebut
# adalah list maka seluruh item dalam list tersebut nilainya bisa
# kita ubah
tuple_mahasiswa[1][0] = 334
print(tuple_mahasiswa[1][0])

# Saat kita mengubah item pada tuple yang sebelumnya adalah list 
# menjadi string maka akan terjadi eror
# TypeError: 'tuple' object does not support item assignment
# tuple_mahasiswa[1] = 'dikyindrah'
# Tipe data berurut

# List
print('\n==========List==========\n')

# List dapat berisi item dengan berbagai macam tipe data
# List berisi integer
list_integer = [5, 7, 3, 9, 12]

# List berisi float
list_float = [6.5, 3.2, 9.12]

# List berisi string
list_string  = ['diky', 'gintoki', 'katsura']

# List berisi boolean
list_boolean = [True, False, False]

# List berisi tipe data campuran
list_campuran = [59, 'gintoki', True]

# Memeriksa apakah suatu item ada pada list
print(5 in list_integer)

# Menampilkan seluruh item pada list
print('\nMenampilkan seluruh item pada list : \n')
print('List berisi integer  :', list_integer)
print('List berisi float    :', list_float)
print('List berisi string   :', list_string)
print('List berisi boolean  :', list_boolean)
print('List berisi campuran :', list_campuran)

# Item pada list bisa di akses menggunakan indeks
print('\nMengakses seluruh item pada list : \n')
print(list_integer[2])
print(list_float[0])
print(list_string[1])
print(list_boolean[2])
print(list_campuran[1])

# List dapat menyimpan variabel sebagai item
print('\nList dapat menyimpan variabel sebagai item :\n')
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

# Item pada list dapat di ubah
print('Item pada list dapat di ubah :\n')
list_bilangan_genap = [4, 3, 8, 12]
# Sebelum di ubah
print('Sebelum di ubah')
print('List bilangan genap:', list_bilangan_genap)

# Setelah di ubah
print('\nSetelah di ubah')
list_bilangan_genap[1] = 6
print('List bilangan genap :', list_bilangan_genap)

# List dapat menyimpan list sebagai item
print('\nList dapat menyimpan list sebagai item :')
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
# Tuple berisi integer
tuple_integer = (12, 37, 89)

# Tuple berisi float
tuple_float = (12.4, 5.5, 30.5)

# Tuple berisi string
tuple_string = ('diky','indra','heramwanto')

# Tuple berisi boolean
tuple_boolean = (False, True, False, True)

# Tuple berisi campuran
tuple_campuran = ('diky', 21, 160.5, False)

# Memeriksa apakah suatu item ada pada tuple
print(5 in tuple_integer)

# Menampilkan seluruh item pada tuple
print('\nMenampilkan seluruh item pada tuple : \n')
print('Tuple berisi integer  :', tuple_integer)
print('Tuple berisi float    :', tuple_float)
print('Tuple berisi string   :', tuple_string)
print('Tuple berisi boolean  :', tuple_boolean)
print('Tuple berisi campuran :', tuple_campuran)

# Item pada tuple bisa di akses menggunakan indeks
print('\nMengakses seluruh item pada tuple : \n')
print(tuple_integer[2])
print(tuple_float[0])
print(tuple_string[1])
print(tuple_boolean[2])
print(tuple_campuran[1])

# Tuple dapat menyimpan variabel sebagai item
print('\nTuple dapat menyimpan variabel sebagai item :\n')
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


# Item pada tuple tidak dapat di ubah
print('Item pada list dapat di ubah :\n')
tuple_bilangan_ganjil = (3, 5, 7, 8)
# Sebelum di ubah
print('Sebelum di ubah')
print('Tuple bilangan ganjil:', tuple_bilangan_ganjil)

# tuple_bilangan_ganjil[3] = 13
# print('Setelah di ubah')
# print('Tuple bilangan ganjil:', tuple_bilangan_ganjil)

# Jika kita mengubah item pada tuple maka akan terjadi eror
# TypeError: 'tuple' object does not support item assignment

# Tuple dapat menyimpan tuple atau list sebagai item
print('\nTuple dapat menyimpan tuple atau list sebagai item :')
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
# adalah list maka seluruh item dalam list tersebut bisa kita ubah
tuple_mahasiswa[1][0] = 334
print(tuple_mahasiswa[1][0])

# Saat kita mengubah item pada tuple yang sebelumnya adalah list 
# menjadi string maka akan terjadi eror
# TypeError: 'tuple' object does not support item assignment
# tuple_mahasiswa[1] = 'dikyindrah'
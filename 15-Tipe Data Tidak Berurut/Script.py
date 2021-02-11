# Tipe data tidak berurut

print('==========Tipe Tidak Berurut==========')

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

# Memeriksa apakah suatu item ada pada set
print(23 in set_integer)

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

# Memeriksa apakah suatu item ada pada set
print(23 in set_integer)

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

# Dictionary dapat berisi item dengan berbagai macam tipe data

# Key pada dictionary bisa dibuat dangan berbagai tipe data kecuali 
# list, set, dan dictionary.

# Key dibuat dengan integer
dictionary_key_integer = {
    1:'processor', 
    2:'motherboard', 
    3:'harddisk', 
    4:'ram', 
    5:'power suply', 
    6:'fan'
}

# Key dibuat dengan float
dictionary_key_float = {21.5:'35 cm', 23.5:'38 cm', 26.5:'42 cm'}

# Key dibuat dengan string
dictionary_key_string = {'deni':19, 'diky':21, 'rudi':25}

# Key dibuat dengan boolean
dictionary_key_boolean = {True:'Yes', False:'No'}

# Key dibuat dengan tuple
dictionary_key_tuple = {(1,):("A"), (2,):("B"), (3):("C")} 

# Key dibuat dengan campuran
dictionary_key_campuran = {1:'HelloWorld', 'warna':'merah', True:1, 85.5:'Baik', (1,):("A")}


# Value pada dictionary bisa dibuat dangan berbagai tipe data
# termasuk list, set, dan dictionary.

# Dictionary dengan value integer
dictionary_value_integer = {'Ayah':45, 'Ibu':40, 'Kakak':18, 'Adik':14}

# Dictionary dengan value float
dictionary_value_float = {'diky':145.5, 'bagus':165.5}

# Dictionary dengan value string
dictionary_value_string = {1:'Diky', 2:'Indra', 3:'Hermawanto'} 

# Dictionary dengan value boolean
dictionary_value_boolean = {0:False, 1:True}

# Dictionary dengan value list
dictionary_value_list = {
    1:['gintoki', 'kagura', 'shinpachi'], 
    2:['hijikata', 'yamazaki', 'okita']
}

# Dictionary dengan value tuple
dictionary_value_tuple = {
    1:('gintoki', 'kagura', 'shinpachi'), 
    2:('hijikata', 'yamazaki', 'okita')
}

# Dictionary dengan value set
dictionary_value_set = {
    1:{'gintoki', 'kagura', 'shinpachi'}, 
    2:{'hijikata', 'yamazaki', 'okita'}
}

# Dictionary dengan value dictionary
dictionary_value_dictionary = {
    1:{1:'gintoki', 2:'kagura', 3:'shinpachi'}, 
    2:{1:'hijikata', 2:'yamazaki', 3:'okita'}
}

# Dictionary dengan value campuran
dictionary_value_campuran = {
    1:21,
    2:175.5,
    3:'dikyindrah',
    4:True,
    5:['Bandar Lampung'],
    6:('Web Developer'),
    7:{'Success'},
    8:{1:'Happy'}
}

print('\nMenampilkan seluruh item pada dictionary : \n')
print('Key pada dictionary bisa dibuat dangan berbagai tipe data kecuali\nlist, set, dan dictionary.\n')
print('Key dibuat dengan integer  :', dictionary_key_integer)
print('Key dibuat dengan float    :', dictionary_key_float)
print('Key dibuat dengan string   :', dictionary_key_string)
print('Key dibuat dengan boolean  :', dictionary_key_boolean)
print('Key dibuat dengan campuran :', dictionary_key_campuran)

print('\nValue pada dictionary bisa dibuat dangan berbagai tipe data termasuk\nlist, set, dan dictionary.\n')
print('Value dibuat dengan integer  :', dictionary_value_integer)
print('Value dibuat dengan float    :', dictionary_value_float)
print('Value dibuat dengan string   :', dictionary_value_string)
print('Value dibuat dengan boolean  :', dictionary_value_boolean)
print('Value dibuat dengan list     :', dictionary_value_list)
print('Value dibuat dengan tuple    :', dictionary_value_tuple)
print('Value dibuat dengan set      :', dictionary_value_set)
print('Value dibuat dengan dictionary  :', dictionary_value_dictionary)
print('Value dibuat dengan campuran :', dictionary_value_campuran)

# Mengakses item pada dictionary
print('\n\nMengakses item pada dictionary :\n')

usia_anggota_keluarga = {'Ayah':45, 'Ibu':40, 'Kakak':18, 'Adik':14}

# Memeriksa apakah suatu item ada pada dictionary
print('Ayah' in usia_anggota_keluarga, '\n')

# Mengakses item pada dictionary menggunakan cara manual
print('Mengakses item pada dictionary menggunakan cara manual :\n')

# Akses item pada dictionary ketika key ada dalam dictionary
print('Usia ibu saat ini adalah', usia_anggota_keluarga['Ibu'], 'tahun')

# # Akses item pada dictionary ketika key tidak ada dalam dictionary
# print('Usia nenek saat ini adalah', usia_anggota_keluarga['Nenek'], 'tahun')

# Mengakses item pada dictionary menggunakan fungsi get()
print('\nMengakses item pada dictionary menggunakan fungsi get() :\n')

# Akses item pada dictionary ketika key ada dalam dictionary
print('Usia ayah saat ini adalah', usia_anggota_keluarga.get('Ayah'), 'tahun')

# Akses item pada dictionary ketika key tidak ada dalam dictionary
print('Usia nenek saat ini adalah', usia_anggota_keluarga.get('Nenek'), 'tahun')

# Mengubah item pada dictionary
print('\n\nMengubah item pada dictionary :\n')

data_diri = {'Nama':'Diky Indra H', 'Umur':21}
print('Sebelum diubah :', data_diri)

# Mengubah item pada dictionary
data_diri['Umur'] = 22

# Menghapus item pada dictionary
print('\n\nMenghapus item pada dictionary :\n')

data_diri = {'Nama':'Diky Indra H', 'Umur':21}
print('Sebelum dihapus :', data_diri, '\n')

# Menghapus item tertentu pada dictionary
data_diri.pop('Umur')
print('Menghapus salah satu item :', data_diri)

# Menghapus seluruh item pada dictionary
data_diri.clear()
print('Menghapus seluruh item :', data_diri, '\n')



# Set dan dictionary bersarang

print('\n==========Set dan Dictionary Bersarang==========')

print('\n==Set Bersarang=====')
set_integer = {(11,12), 
               (13,14), 
               (15,16)}

print(set_integer)

print('\n==Dictionary Bersarang=====')
dict_minuman = {'nama_minuman':{1:'Sprite', 2:'Coca-cola', 3:'Frutea'},
                'harga_minuman':{1:12000, 2:10000, 3:7000}}

print('\n==Mengakses Item Pada Dictionary Bersarang=====')
print(dict_minuman['nama_minuman'][1])
print(dict_minuman['harga_minuman'][1])

print('\n==Menambah, Mengubah, dan Menghapus Item Pada Dictionary Bersarang=====')
print('\n==Menambah Item Pada Dictionary Bersarang=====')

# Cara pertama
dict_minuman['nama_minuman'][4] = 'Mizone'
dict_minuman['harga_minuman'][4] = 8500

print(dict_minuman)

# Cara kedua
dict_minuman['nama_minuman'].update({5:'Ale-ale'})
dict_minuman['harga_minuman'].update({5:1000})

print(dict_minuman)

print('\n==Mengubah Item Pada Dictionary Bersarang=====')

# Cara petama
dict_minuman['nama_minuman'][2] = 'Mogu-gogu'
dict_minuman['harga_minuman'][2] = 5500

print(dict_minuman)

# Cara keuda
dict_minuman['nama_minuman'].update({2:'Mogu-gogu'})
dict_minuman['harga_minuman'].update({2:5500})

print(dict_minuman)

print('\n==Menghapus Item Pada Dictionary Bersarang=====')

# Menghapus salah satu item
# Cara pertama
dict_minuman['nama_minuman'].pop(1)
dict_minuman['harga_minuman'].pop(1)

print(dict_minuman)

# Cara kedua
del dict_minuman['nama_minuman'][2]
del dict_minuman['harga_minuman'][2]

print(dict_minuman)

# Menghapus seluruh item
dict_minuman.clear()

print(dict_minuman)


print('\n==Perulangan Pada Dictionary Bersarang=====')
print('\nCara Pertama')
for menu, daftar_menu in dict_minuman.items():
    print(menu)
    print('==========')
    for no in daftar_menu.keys():
        print(no, daftar_menu[no])
    print('')

print('\nCara Kedua')
lenght = int((len(dict_minuman['nama_minuman'])+len(dict_minuman['harga_minuman']))/2)
i = 1
while i <= lenght:
    print(i, dict_minuman['nama_minuman'][i], dict_minuman['harga_minuman'][i])
    i = i + 1


# dictionary_buah = {'a':{1:'apel', 2:'anggur', 3:'mangga'},
#                    'b':{1:'jeruk',2:'nanas'},
#                    'c':'manggis'}

# for menu, daftar_menu in dictionary_buah.items():
#     print(menu)
#     print('==========')
#     if type(dictionary_buah[menu]) is dict:
#         for no in daftar_menu.keys():
#             print(daftar_menu[no])
#     else:
#         print(dictionary_buah[menu])
#     print('')
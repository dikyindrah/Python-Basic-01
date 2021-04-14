# Set dan dictionary bersarang

print('\n==========Set dan Dictionary Bersarang==========')

print('\n==Set Bersarang=====')
set_integer = {(11,12), 
               (13,14), 
               (15,16)}

print(set_integer)

print('\n==Dictionary Bersarang=====')
dictionary_mesin_minuman = {'minuman':{1:'Sprite', 2:'Coca-cola', 3:'Frutea'},
                            'harga':{1:12000, 2:10000, 3:7000}}

for menu, daftar_menu in dictionary_mesin_minuman.items():
    print(menu)
    print('==========')
    for no in daftar_menu.keys():
        print(no, daftar_menu[no])
    print('')


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
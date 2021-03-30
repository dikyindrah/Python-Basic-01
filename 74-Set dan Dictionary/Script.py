# Set dan dictionary
print('\n==========Set dan Dictionary==========\n')
print('==Set==========\n')

set_integer = {10, 20, 30, 40, 50}
set_float = {1.0, 2.5, 10.55, 5.5, 4.5}
set_boolean = {True, False, True, False}
set_string = {'aku', 'sedang', 'belajar', 'python'}
set_campuran = {10, 1.0, True, 'python'}

print(set_integer)
print(set_float)
print(set_boolean)
print(set_string)
print(set_campuran)

print('\n==Mengisi Set Dengan Tipe Data List dan Tuple==========\n')

list_integer = [60, 70, 80, 90, 100]
set_integer = {10, 20, 30, 40, 50} 

print(list_integer, type(list_integer))
print(set_integer, type(set_integer))

# Mengubah tipe data list ke set
item_baru = set(list_integer)
# Menambahkan item baru kedalam set_integer
set_integer.update(item_baru)

print(set_integer, '\n')

tuple_string = ('python',)
set_string = {'aku', 'sedang', 'belajar'}

print(tuple_string, type(tuple_string))
print(set_string, type(set_string))

# Mengubah tipe data tuple ke set
item_baru = set(tuple_string)
# Menambahkan item baru kedalam set_string
set_string.update(item_baru)

print(set_string)

print('\n==Set Kosong==========\n')

set_kosong = set()
print(set_kosong, type(set_kosong))

print('\n==Set Memiliki Item Yang Unik==========\n')

set_dengan_item_yang_sama = {100, 100, 30, 30, 10, 30, 10, 20, 30, 20, 20}
print(set_dengan_item_yang_sama, type(set_dengan_item_yang_sama))


print('\n==Dictionary==========\n')
print('==Dictionary Key==========\n')

# Dictionary kosong
dictionary_kosong = {}

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
dictionary_key_campuran = {1:'HelloWorld', 
                           'warna':'merah', 
                            True:1, 
                            85.5:'Baik', 
                            (1,):("A")}

print('\n', dictionary_kosong, type(dictionary_kosong))
print('\n', dictionary_key_integer, type(dictionary_key_integer))
print('\n', dictionary_key_float, type(dictionary_key_float))
print('\n', dictionary_key_string, type(dictionary_key_string))
print('\n', dictionary_key_boolean, type(dictionary_key_boolean))
print('\n', dictionary_key_tuple, type(dictionary_key_tuple))
print('\n', dictionary_key_campuran, type(dictionary_key_campuran))

print('==Dictionary Value==========\n')

# Dictionary kosong
dictionary_kosong = {}

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

print('\n', dictionary_kosong, type(dictionary_kosong))
print('\n', dictionary_value_integer, type(dictionary_value_integer))
print('\n', dictionary_value_float, type(dictionary_value_float))
print('\n', dictionary_value_string, type(dictionary_value_string))
print('\n', dictionary_value_boolean, type(dictionary_value_boolean))
print('\n', dictionary_value_campuran, type(dictionary_value_campuran))
print('\n', dictionary_value_list, type(dictionary_value_list))
print('\n', dictionary_value_tuple, type(dictionary_value_tuple))
print('\n', dictionary_value_set, type(dictionary_value_set))
print('\n', dictionary_value_dictionary, type(dictionary_value_dictionary))




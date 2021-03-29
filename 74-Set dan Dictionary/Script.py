# Set dan dictionary
print('\n==========Set dan Dictionary==========\n')
print('==========Set==========\n')

set_kosong = {}
set_integer = {10, 20, 30, 40, 50}
set_float = {1.0, 2.5, 10.55, 5.5, 4.5}
set_boolean = {True, False, True, False}
set_string = {'aku', 'sedang', 'belajar', 'python'}
set_campuran = {10, 1.0, True, 'python'}

print(set_kosong)
print(set_integer)
print(set_float)
print(set_boolean)
print(set_string)
print(set_campuran)

print('\n==========Mengisi Set Dengan Tipe Data List dan Tuple==========\n')

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

print('\n==========Set Kosong==========\n')
set_kosong = set()
print(set_kosong, type(set_kosong))

print('\n==========Set Memiliki Item Yang Unik==========\n')

set_dengan_item_yang_sama = {100, 100, 30, 30, 10, 30, 10, 20, 30, 20, 20}
print(set_dengan_item_yang_sama, type(set_dengan_item_yang_sama))
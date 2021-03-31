# Menambah, mengubah, dan menghapus item pada set dan dictionary

print('\n==========Menambah, Mengubah, dan Menghapus Item Pada Set dan Dictionary==========')
print('\n==Set==========')
set_integer = {10, 20, 30, 40, 50}
print(set_integer)

print('\n==Menambah Item Pada Set==========')

# Menambah satu item
set_integer.add(60)
print(set_integer)

# Menambah beberapa item sekaligus
set_integer.update({70, 80, 90, 100})
print(set_integer)

print('\n==Menghapus Item Pada Set==========')

# Menghapus salah satu item
# Cara pertama
set_integer.remove(70)
print(set_integer)

# Cara kedua
set_integer.discard(100)
print(set_integer)

# Menghapus seluruh item
set_integer.clear()
print(set_integer)


print('\n==Dictionary==========')
dictionary_hari = {1:'Senin', 2:'Selasa'}
print(dictionary_hari)

print('\n==Menambah Item Pada Dictionary==========')
# Menambah satu item
dictionary_hari[3] = 'Rabu'
print(dictionary_hari)

# Menambah beberapa item sekaligus
dictionary_hari.update({4:'Kamis', 5:'Jumat', 6:'Sabtu', 7:'Minggu'})
print(dictionary_hari)

print('\n==Mengubah Item Pada Dictionary==========')
# Cara pertama 
dictionary_hari[1] = 'Sekarang adalah hari senin'
print(dictionary_hari)

# Cara cara kedua 
dictionary_hari.update({2:'Besok adalah hari selasa'})
print(dictionary_hari)

print('\n==Menghapus Item Pada Dictionary==========')

# Menghapus salah satu
dictionary_hari.pop(1)
print(dictionary_hari)

# Menghapus seluruh item
dictionary_hari.clear()
print(dictionary_hari)

print('')
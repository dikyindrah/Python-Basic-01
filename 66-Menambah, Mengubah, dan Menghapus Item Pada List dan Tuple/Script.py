# Menambah, mengubah, dan menghapus item pada list dan tuple

print('\n==========Menambah, Mengubah, dan Menghapus Item Pada List dan Tuple==========\n')

print('\n==Menambah, Mengubah, dan Menghapus Item Pada List=====\n')

list_integer = [10, 20, 30, 40, 50]
print('list_integer = ', list_integer)

print('\n==Menambah Item=====')

# Menambah satu item
list_integer.append(60)
print('list_integer = ', list_integer)

# Menambah beberapa item sekaligus
list_integer.extend([70, 90, 100])
print('list_integer = ', list_integer)

print('\n==Mengubah Item=====')

# list_integer[0] = 100
# print('list_integer = ', list_integer)

list_integer.insert(0, 100)
print('list_integer = ', list_integer)

print('\n==Menghapus Item=====')
print('\nMenghapus Salah Satu Item:')
# Cara pertama
list_integer.pop(1)
print('list_integer = ', list_integer)

# Cara kedua
del list_integer[3]
del list_integer[4]
print('list_integer = ', list_integer)

print('\nMenghapus Seluruh Item:')
list_integer.clear()
print('list_integer = ', list_integer)

print('\n==Menambah, Mengubah, dan Menghapus Item Pada Tuple=====\n')

tuple_string = ('aku', 'sedang')
print(tuple_string)

list_string = list(tuple_string)

list_string.append('belajar')
list_string.append('python')
print(list_string)

tuple_string = tuple(list_string)
print(tuple_string)



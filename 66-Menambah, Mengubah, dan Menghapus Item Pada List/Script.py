# Menambah, mengubah, dan menghapus item pada list

print('\n==========Menambah, Mengubah, dan Menghapus Item Pada List==========\n')

list_integer = [10, 20, 30, 40, 50]
print('list_integer = ', list_integer)

print('\n==Menambah Item=====')
list_integer.append(60)
print('list_integer = ', list_integer)

print('\n==Mengubah Item=====')

# list_integer[0] = 100
# print('list_integer = ', list_integer)

list_integer.insert(0, 100)
print('list_integer = ', list_integer)

print('\n==Menghapus Item=====')
print('\nMenghapus Salah Satu Item:')
list_integer.pop(1)
print('list_integer = ', list_integer)

print('\nMenghapus Seluruh Item:')
list_integer.clear()
print('list_integer = ', list_integer)


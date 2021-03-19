# Perulangan pada list

print('\n==========Perulangan Pada List==========\n')

list_integer = [10, 20, 30, 40, 50]
print('list_integer = ', list_integer)

list_kosong = []
print('list_kosong = ', list_kosong)

print('\n==Menampilkan Item Pada List Menggunakan Perulangan=====')

for item in list_integer:
    print(item)

print('\n==Menambahkan Item Pada List Menggunakan Perulangan=====')

for i in range(1, 10+1):
    list_kosong.append(i)

print('\nlist_kosong =', list_kosong)
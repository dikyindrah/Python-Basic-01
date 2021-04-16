# list dan tuple bersarangs bersarang

print('\n==========List dan Tuple Bersarang==========\n')

print('\n==List Bersarang=====\n')
print('\n==Mengakses Item Pada List Bersarang=====\n')
list_a = [[1,2,3], [4,5,6], [7,8,9]]
print(list_a, '\n')

print(list_a[0][0], list_a[0][1], list_a[0][2])
print(list_a[1][0], list_a[1][1], list_a[1][2])
print(list_a[2][0], list_a[2][1], list_a[2][2])

print('\n==Menambah Item Pada List Bersarang=====\n')
# Menambah item pada list bersarang yang sudah ada
list_a[0].append(4)

# Menambah item pada list bersarang baru
list_a.append([])
list_a[3].append(10)
list_a[3].append(11)
list_a[3].append(12)

list_a.append([12,14,15])
print(list_a, '\n')

print('\n==Mengubah Item Pada List Bersarang=====\n')
list_b = [[1,2,3], [4,5,6], [7,8,9]]
print(list_b)

# Cara pertama
list_b[0][0] = 100
print(list_b)

# Cara kedua
list_b[1].insert(0, 400)
print(list_b)

print('\n==Menghapus Item Pada List Bersarang=====\n')
# Menghapus salah satu item
list_c = [[1,2,3], [4,5,6], [7,8,9]]
print(list_c)

# Cara petama
list_c[0].pop(2)
print(list_c)

list_c.pop(1)
print(list_c)

# Cara kedua
del list_c[1][1]
print(list_c)

del list_c[1]
print(list_c)

# Menghapus seluruh item 
list_d = [[1,2,3], [4,5,6], [7,8,9]]
print(list_d)

list_d[0].clear()
print(list_d)

list_d.clear()
print(list_d)

print('\n==Menampilkan Item Pada List Bersarang Menggunakan Perulangan 1=====\n')
for x in range(len(list_a)):
    for y in range(len(list_a)):
        print(list_a[x][y], end=' ')
    print('')

print('\n==Menampilkan Item Pada List Bersarang Menggunakan Perulangan 2=====\n')

list_b = [[[10, 11, 12], [13, 14, 15], [16, 17, 18]],
          [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
          [[28, 29, 30], [31, 32, 33], [34, 35, 36]]]

for x in range(len(list_b)):
    for y in range(len(list_b)):
        for z in range(len(list_b)):
            print(list_b[x][y][z],end=' ')
    print('')


print('\n==Tuple Bersarang=====\n')
print('\n==Menampilkan Item Pada Tuple Bersarang 1=====\n')

tuple_a = (('Pisang', 'Anggur', 'Semangka'), 
                ('Jeruk', 'Apel'),
                ('Stroberi',))

print(tuple_a[0][0], tuple_a[0][1], tuple_a[0][2])
print(tuple_a[1][0], tuple_a[1][1])
print(tuple_a[2][0])

print('\n==Menampilkan Item Pada Tuple Bersarang Menggunakan Perulangan 1=====\n')

for x in range(len(tuple_a)):
    for y in range(len(tuple_a[x])):
        print(tuple_a[x][y], end=' ')
    print('')

print('\n==Menampilkan Item Pada tuple Bersarang Menggunakan Perulanga 2=====\n')

tuple_b = (((10, 11, 12), (13, 14, 15), (16, 17, 18)),
           ((19, 20, 21), (22, 23, 24), (25, 26, 27)),
           ((28, 29, 30), (31, 32, 33), (34, 35, 36)))

for x in range(len(tuple_b)):
    for y in range(len(tuple_b)):
        for z in range(len(tuple_b)):
            print(tuple_b[x][y][z],end=' ')
    print('')
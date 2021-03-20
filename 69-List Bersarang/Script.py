# list Bersarang

print('\n==========List Bersarang==========\n')

print('\n==Menampilkan Item Pada List Bersarang=====\n')
list_a = [[1,2,3], [4,5,6], [7,8,9]]
print(list_a, '\n')

print(list_a[0][0], list_a[0][1], list_a[0][2])
print(list_a[1][0], list_a[1][1], list_a[1][2])
print(list_a[2][0], list_a[2][1], list_a[2][2])

print('\n==Menampilkan Item Pada List Bersarang Menggunakan Perulangan=====\n')
for x in range(len(list_a)):
    for y in range(len(list_a)):
        print(list_a[x][y], end=' ')
    print('')

print('\n==Menampilkan Item Pada List Bersarang=====\n')
list_b = [[[10, 20, 30]], [[40, 50, 60]], [[70, 80, 90]]]

print(list_b[0][0][0], list_b[0][0][1], list_b[0][0][2],)
print(list_b[1][0][0], list_b[1][0][1], list_b[1][0][2],)
print(list_b[2][0][0], list_b[2][0][1], list_b[2][0][2],)

print('\n==Menampilkan Item Pada List Bersarang Menggunakan Perulangan=====\n')
for x in range(len(list_b)):
    for y in range(len(list_b[0])):
        for z in range(len(list_b)):
            print(list_b[x][y][z], end=' ')
        print('')


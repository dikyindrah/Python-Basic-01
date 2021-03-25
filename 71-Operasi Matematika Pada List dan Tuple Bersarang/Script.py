# Operasi matematika pada list dan tuple bersarang

print('\n==========Operasi Matematika Pada List dan Tuple Bersarang==========\n')

# Fungsi untuk menampilkan item
def item(lt_x):
    for x in range(len(lt_x)):
        for y in range(len(lt_x[x])):
            print(lt_x[x][y], end=' ')
        print('')
    print('')    

# Fungsi untuk menampilkan indeks item
def index(lt_x):
    for x in range(len(lt_x)):
        for y in range(len(lt_x[x])):
            print('[', x, y, ']', end=' ')
        print('')
    print('')


print('\n==Operasi Matematika Pada List Bersarang=====\n')

list_a = [[10, 11, 12], 
          [13, 14, 15]]

list_b = [[16, 17, 18], 
          [19, 20, 21]]

# List_c adalah hasil penjumlahan item list_a dengan list_b
list_c = []
p_x = int((len(list_a) + len(list_b))/2)
p_y = int((len(list_a[0]) + len(list_b[1]))/2)

for x in range(p_x):
    for y in range(p_y):
        if len(list_c) < x+1:
            list_c.append([])

        tmp = list_a[x][y] + list_b[x][y]
        list_c[x].append(tmp)

print('==list_a=====\n')
item(list_a)
print('==Indeks list_a=====\n')
index(list_a)

print('==list_b=====\n')
item(list_b)
print('==Indeks list_b=====\n')
index(list_b)

print('==list_c=====\n')
item(list_c)
print('==Indeks list_c=====\n')
index(list_c)

print('\n==Operasi Matematika Pada Tuple Bersarang=====\n')

tuple_a = ((21, 22, 23), 
           (24, 25, 26))

tuple_b = ((27, 28, 29), 
           (30, 31, 32))

# List_c adalah hasil penjumlahan item tuple_a dengan tuple_b
list_c = []
p_x = int((len(tuple_a) + len(tuple_b))/2)
p_y = int((len(tuple_a[0]) + len(tuple_b[1]))/2)

for x in range(p_x):
    for y in range(p_y):
        if len(list_c) < x+1:
            list_c.append([])

        tmp = tuple_a[x][y] + tuple_b[x][y]
        list_c[x].append(tmp)

tuple_c = tuple(list_c)

print('==tuple_a=====\n')
item(tuple_a)
print('==Indeks tuple_a=====\n')
index(tuple_a)

print('==tuple_b=====\n')
item(tuple_b)
print('==Indeks tuple_b=====\n')
index(tuple_b)

print('==tuple_c=====\n')
item(tuple_c)
print('==Indeks tuple_c=====\n')
index(tuple_c)
# Operasi matematika pada list dan tuple

print('\n==========Operasi Matematika Pada List==========')

print('\n==Menghitung Total Nilai Pada List=====\n')
list_nilai = [10, 20, 30, 40, 50]
total_nilai = 0

for item in list_nilai:
    total_nilai = total_nilai + item

print('nilai =', list_nilai)
print('total =', total_nilai)

print('\n==Menghitung Item Pada Dua List Yang Berbeda=====\n')

list_x = [10, 20, 30]
list_y = [10, 20, 30]

total = list_x[0] + list_y[0]
print(total)

list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
list_c = []

panjang = int((len(list_a) + len(list_b)) / 2)

for i in range(panjang):
    tmp = list_a[i] + list_b[i]
    list_c.append(tmp)

print(list_a)
print(list_b)
print('----------------- +')
print(list_c)


print('\n==Menghitung Total Nilai Pada Tuple=====\n')

tuple_integer = (1, 2, 3, 4, 5)
total_nilai = 0

for item in tuple_integer:
    total_nilai = total_nilai + item

print('tuple_integer =', tuple_integer)
print('total_nilai =', total_nilai)

print('\n==Menghitung Item Pada Dua Tuple Yang Berbeda=====\n')

tuple_a = (1, 2, 3, 4, 5)
tuple_b = (6, 7, 8, 9, 10)
list_c = []

panjang = int((len(tuple_a) + len(tuple_b))/2)

for i in range(panjang):
    tmp = tuple_a[i] + tuple_b[i]
    list_c.append(tmp)

tuple_c = tuple(list_c)

print(tuple_a)
print(tuple_b)
print('----------------- +')
print(tuple_c)



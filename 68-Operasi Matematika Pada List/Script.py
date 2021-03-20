# Operasi matematika pada list

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

list_A = [1, 2, 3, 4, 5]
list_B = [6, 7, 8, 9, 10]
list_C = []

panjang = int((len(list_A) + len(list_B)) / 2)

for i in range(panjang):
    tmp = list_A[i] + list_B[i]
    list_C.append(tmp)

print(list_A)
print(list_B)
print('----------------- +')
print(list_C)



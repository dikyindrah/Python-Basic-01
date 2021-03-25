# latihan membuat program perkalian matriks
matriks_a = [[1, 2],
             [3, 4]]

matriks_b = [[5, 6],
             [7, 8]]


'''
==Index=====
[0 0]*[0 0] + [0 1]*[1 0]   [0 0]*[0 1] + [0 1]*[1 1]

[1 0]*[0 0] + [1 1]*[1 0]   [1 0]*[0 1] + [1 1]*[1 1]

==Item=====
1*5 + 2*7   1*6 + 2*8

3*5 + 4*7   3*6 + 4*8

==Output=====
19   22
43   50
'''

matriks_c = []

# Hitung matriks
tmp = 0 
for x in range(len(matriks_a)):
    for y in range(len(matriks_a[x])):
        for z in range(len(matriks_a[y])):
            if len(matriks_c) < x+1:
                matriks_c.append([])

            num = matriks_a[x][z] * matriks_b[z][y]
            tmp = tmp + num
        matriks_c[x].append(tmp)
        tmp = 0

# Tampilkan hasil perhitungan matriks
for x in range(len(matriks_c)):
    for y in range(len(matriks_c[x])):
        print(matriks_c[x][y], end=' ')
    print('')






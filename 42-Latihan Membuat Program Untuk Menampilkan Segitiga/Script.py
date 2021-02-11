# Program untuk menampilkan segitiga

print('\n==========Segitiga==========\n')

obj = 1

for row in range(6+1, 0, -1):
    for col in range(row):
        print(' ', end='')
    for print_obj in range(obj):
        print('#', end='')
    obj+=2
    print('') 
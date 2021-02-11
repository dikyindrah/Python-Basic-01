# Program untuk menampilkan belah ketupat

print('\n==========Belah Ketupat==========\n')

obj_1 = 1
for row_1 in range(6, 0, -1):
    for col_1 in range(row_1):
        print(' ', end='')
    for print_obj_1 in range(obj_1):
        print('#', end='')
    obj_1+=2
    if row_1 == 1:
        obj_2 = 9
        print('')
        for row_2 in range(2, 6+1, 1):
            for col_2 in range(row_2):
                print(' ', end='')
            for print_obj_2 in range(obj_2):
                print('#', end='')
            obj_2-=2
            print('')
    print('') 
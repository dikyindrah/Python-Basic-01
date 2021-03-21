# Mengakses item pada list dan tuple

print('\n==========Mengakses Item Pada List dan Tuple==========')

print('\n==Mengakses Item Pada List=====\n')
list_string = ['aku', 'sedang', 'belajar', 'python']

print(list_string[0])
print(list_string[1])
print(list_string[2])
print(list_string[3])

print('')

# Akses list menggunakan for
for item in list_string:
    print(item)

print('')

# Akses list menggunakan while
i = 0
l = len(list_string)
while i < l:
    print(list_string[i])
    i = i + 1

print('\n==Mengakses Item Pada Tuple=====\n')

tuple_integer = (10, 20, 30, 40, 50)

print(tuple_integer[0])
print(tuple_integer[1])
print(tuple_integer[2])
print(tuple_integer[3])
print(tuple_integer[4])

print('')

# Akses tuple menggunakan for
for item in tuple_integer:
    print(item)

print('')

# Akses tuple menggunakan while
i = 0
l = len(tuple_integer)
while i < l:
    print(tuple_integer[i])
    i = i + 1
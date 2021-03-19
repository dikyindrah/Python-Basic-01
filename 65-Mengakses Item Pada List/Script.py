# Mengakses item pada list

print('\n==========Mengakses Item Pada List==========\n')

list_string = ['aku', 'sedang', 'belajar', 'python']

print(list_string[0])
print(list_string[1])
print(list_string[2])
print(list_string[3])

# Akses list menggunakan for
for item in list_string:
    print(item)

# Akses list menggunakan while
i = 0
l = len(list_string)
while i < l:
    print(i, list_string[i])
    i = i + 1
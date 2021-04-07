# Perulangan pada set dan dictionary
print('\n==========Perulangan Pada Set==========')
set_integer = {10, 20, 30, 40, 50}

# Cara pertama
for item in set_integer:
    print(item, end=' ')

print('')

# Cara kedua
for i in range(len(set_integer)):
    print(list(set_integer)[i], end=' ')

print('')

# Cara ketiga
i = 0 
while i < len(set_integer):
    print(list(set_integer)[i], end=' ')
    i = i + 1


print('\n\n==========Perulangan Pada Dictionary==========')
# Menambah item
dictionary_kosong = {}
list_string = ['aku', 'sedang', 'belajar', 'python']

for i in range(len(list_string)):
    dictionary_kosong[i] = list_string[i]
    # dictionary_kosong.update({i:list_string[i]})

print(dictionary_kosong)

# Menampilkan item
dictionary_hari = {1:'Senin', 
                   2:'Selasa', 
                   3:'Rabu', 
                   4:'Kamis', 
                   5:'Jumat', 
                   6:'Sabtu', 
                   7:'Minggu'}

# Cara pertama    
for key in dictionary_hari.keys():
    print(key, end=' ' )

print('')

for value in dictionary_hari.values():
    print(value, end=' ')

print('')

# Cara kedua
for key, value in dictionary_hari.items():
    print(key, value, end=' ')

print('')
# Cara ketiga
i = 0
while i < len(dictionary_hari):
    key = list(dictionary_hari.keys())
    print(key[i], dictionary_hari[key[i]], end=' ')
    i = i + 1

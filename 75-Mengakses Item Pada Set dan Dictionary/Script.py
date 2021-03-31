# Mengakses item pada set dan dictionary

print('\n==========Mengakses Item Pada Set dan Dictionary==========')

print('\n==Set==========\n')
set_string = {'aku', 'sedang', 'belajar', 'python'}
print(set_string)

# Cara pertama
print(list(set_string)[0])

# Cara kedua
list_string = list(set_string)
print(list_string)
print(list_string[1])

print('\n==Dictionary==========\n')
dictionary_hari = {1:'Senin', 2:'Selasa', 3:'Rabu',
                   4:'Kamis', 5:'Jumat', 6:'Sabtu', 
                   7:'Minggu'}


# Cara pertama
print(dictionary_hari[1])
print(dictionary_hari[2])
print(dictionary_hari[3])
print(dictionary_hari[4])
print(dictionary_hari[5])
print(dictionary_hari[6])
print(dictionary_hari[7])

# Cara Kedua
print(dictionary_hari.get(1))
print(dictionary_hari.get(8))
# print(dictionary_hari[8])

print(dictionary_hari.get(10, 'Hari tidak ditemukan.'))

print('')


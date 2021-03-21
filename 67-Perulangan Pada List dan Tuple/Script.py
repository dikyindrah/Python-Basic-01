# Perulangan pada list dan tuple

print('\n==========Perulangan Pada List==========\n')

list_kosong = []
print('list_kosong = ', list_kosong)

# Menambah item pada list
for i in range(10, 50+1, 10):
    list_kosong.append(i)

# Menampilkan item pada list
for item in list_kosong:
    print(item,end=' ')

print('')

tuple_string = ('aku', 'sedang', 'belajar', 'python')

for item in tuple_string:
    print(item,end=' ')
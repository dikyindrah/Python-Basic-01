# Tipe data teks
# String

username = 'diky'
password = 'hello12345'

print(username)
print(password)

username = "indrah"
password = "world12345"

print(username)
print(password)


nama = 'dikyindrah'
print('\n' + nama)

# Memeriksa jenis data pada variabel
print('Jenis data pada', nama, 'adalah :', type(nama))

# Memeriksa panjang string
print('Panjang string adalah :', len(nama), 'karakter')

# Indeks
# Dari depan
print('\n' + nama[0])
print(nama[1])
print(nama[2])
print(nama[3] + '\n')

# Dari belakang
print(nama[-1])
print(nama[-2])
print(nama[-3])
print(nama[-4]+ '\n')

# Substring
# Dari depan
print(nama[0:10])
print(nama[3:7])
print(nama[4:8])

# Dari belakang
print('\n' + nama[-4:-1])
print(nama[-8:-3] + '\n')

# Melewati beberapa karakter
print(nama[0:10:3])
print(nama[-10:-1:3])
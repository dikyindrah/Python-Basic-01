# Fungsi lambda

print('==========Fungsi Lambda==========\n')

# Fungsi lambda dengan satu parameter
kuadrad = lambda x: x * x
print(kuadrad(2))

# Fungsi lambda dengan dua parameter
perkalian = lambda x, y: x * y
print(perkalian(5, 2))

print('')

# Menggunakan fungsi lambda sebagai argumen ke fungsi tingkat
# tinggi
def nilai(func):
    n_x = 5
    n_y = 5

    return func(n_x, n_y)

penjumlahan = lambda x, y: x + y

print(nilai(penjumlahan))

print('')

list_angka = [5, 7, 6, 4, 1, 3, 9, 10]

# Menggunakan fungsi lambda sebagai argumen pada fungsi
# filter()
angka_genap = lambda x: x % 2 == 0

list_angka_genap = list(filter(angka_genap, list_angka))
print(list_angka_genap)

# Menggunakan fungsi lambda sebagai argumen pada fungsi
# map()
kalikan_angka = lambda x: x * 2

list_angka_hasil_kali = list(map(kalikan_angka, list_angka))
print(list_angka_hasil_kali)


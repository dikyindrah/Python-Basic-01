# Passing paramenter

print('==========Passing Parameter==========\n')

print('Pass by Value\n')
nilai = 10

def penjumlahan(x):
    print(x + 10)

# Sebelum memanggil fungsi penjumalan()
print(nilai)

# Saat memanggil fungsi penjumalan()
penjumlahan(nilai)

# Setelah memanggil fungsi penjumalan()
print(nilai)

# Mengubah nilai pada variabel asli
nilai = 50
print(nilai)

print('\nPass by Reference\n')

list_angka = [1, 2, 3, 4, 5]

def ubah_angka(angka):
    angka[4] = 71
    return angka

# Sebelum memanggil fungsi ubah_angka()
print(list_angka)

# Saat memanggil fungsi ubah_angka()
print(ubah_angka(list_angka))

# SEtelah memanggil fungsi ubah_angka()
print(list_angka)

# Mengubah angka pada variable asli
list_angka[1] = 155
print(list_angka)
print(ubah_angka(list_angka))

def print_teks():
    global teks

    for i in range(3):
        if i == 2:
            teks = 'Hello Python'
            print(teks)
        else:
            print(teks)

# Sebelum memanggil fungsi print_teks()
teks = 'Hello World'

# Saat memanggil fungsi print_teks()
print_teks()

# Setelah memanggil fungsi print_teks()
print(teks)
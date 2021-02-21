# Operasi pada fungsi

print('==========Operasi Pada Fungsi==========\n')

# Memanggil fungsi yang mengembalikan nilai
def tampilkan_angka(angka):
    return angka

# Panggil fungsi (cara 1)
print(tampilkan_angka(5))

# Panggil fungsi (cara 2)
hasil = tampilkan_angka(5)
print(hasil)

# Panggil fungsi (cara 3 SALAH)
# Cara ini tidak akan menghasilkan apapun
tampilkan_angka(5)

print('')

# Memanggil fungsi yang tidak mengembalikan nilai
def tampilkan_teks(teks):
    print(teks)

# Panggil fungsi (cara 1)
tampilkan_teks('Hello World')

# Panggil fungsi (cara 2)
hasil = tampilkan_angka('Hello World')
print(hasil)

# Panggil fungsi (cara 3 SALAH)
# Cara ini akan menghasilkan nilai none
print(tampilkan_teks('Hello World'))

# Meneruskan fungsi sebagai argumen
def penjumlahan(x, y):
    return x + y

def nilai(func_penjumlahan):
    n_x = 5
    n_y = 5
    return func_penjumlahan(n_x, n_y)

print(nilai(penjumlahan))

print('')

# Menetapkan fungsi kedalam variabel
def tampilkan_teks(teks):
    print(teks)

t_teks = tampilkan_teks

t_teks('Hello World')

print('')

# Menetapkan nilai kembalian dari fungsi kedalam variabel
def jumlah(x, y):
    return x + y

hasil_jumlah = jumlah(5, 5)

print(hasil_jumlah)


print('')

# Mendefinisikan fungsi di dalam fungsi lain
def tampilkan_teks(teks):
    def tampilkan():
        print(teks)
    
    tampilkan()

tampilkan_teks('Hello World')

print('')

# Mengembalikan Fungsi
def perkalian():
    def hitung_perkalian():
        hasil_perkalian = 5 * 5
        return hasil_perkalian
    
    return hitung_perkalian()

print(perkalian())

print('')

# Memanggil fungsi di dalam fungsi lain
list_nilai = [10, 20, 30, 40, 50]

def hitung_total_nilai(nilai):
    total_nilai = 0

    for item in nilai:
        total_nilai = total_nilai + item

    return total_nilai

def tampilkan_total_nilai():
    print(hitung_total_nilai(list_nilai))

tampilkan_total_nilai()     

print('')


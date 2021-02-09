#  Fungsi bersarang

print('==========Fungsi Bersarang==========')

# Fungsi bagian luar (Outer function)
def tampilkan_teks(teks):
    isi_teks = teks

    # fungsi bagian dalam (Inner Function)
    def tampil():
        print(isi_teks)
    
    # Memanggil fungsi bagian dalam tampil()
    tampil()

# Memanggil fungsi baigian luar tampilkan_teks()
tampilkan_teks(teks='Selamat malam!')

print('')

# Scope (Ruang lingkup) variabel pada fungsi bersarang
def fungsi_bagian_luar():
    angka_pertama = 1

    def fungsi_bagian_dalam():
        angka_kedua = 2
        print(angka_pertama)
        print(angka_kedua)

    fungsi_bagian_dalam()
    print(angka_pertama)
    # Variabel angka_kedua tidak bisa diakses di luar fungsi bagian dalam
    # print(angka_kedua)`

fungsi_bagian_luar()

print('')

# Mengubah nilai variable pada fungsi bagian luar di fungsi bagian dalam
def f1():
    teks = 'hello world'
    
    def f2():
        teks = 'i love python'
        print(teks)

    # Sebelum memanggil fungsi f2()
    print(teks)
    
    # Saat memanggil fungsi f2()
    f2()

    # Setelah memanggil fungsi f2()
    print(teks)

# Memanggil fungsi f1()
f1()

print('')

# Mengubah nilai variable pada fungsi bagian luar di fungsi bagian dalam
# dengan mereferensikan nilai variabel menggunakan list

def f1():
    teks = ['hello world']
    
    def f2():
        teks[0] = ['i love python']
        print(teks)

    # Sebelum memanggil fungsi f2()
    print(teks)
    
    # Saat memanggil fungsi f2()
    f2()

    # Setelah memanggil fungsi f2()
    print(teks)

# Memanggil fungsi f1()
f1()

print('')

# Mengubah nilai variable pada fungsi bagian luar di fungsi bagian dalam
# dengan mereferensikan nilai variabel menggunakan kata kunci nonlokal

def f1():
    teks = 'hello world'

    def f2():
        nonlocal teks 
        teks = 'i love pyhton'
        print(teks)

    # Sebelum memanggil fungsi f2()
    print(teks)

    # Saat memanggil fungsi f2()
    f2()
    
    # Stelah memanggil fungsi f2()
    print(teks)

f1()

print('')

# Mengubah nilai variable pada fungsi bagian luar di fungsi bagian dalam
# dengan mereferensikan nilai variabel menggunakan nama fungsi
def f1():
    f1.teks = 'hello world'

    def f2():
        f1.teks = 'i love pyhton'
        print(f1.teks)

    # Sebelum memanggil fungsi f2()
    print(f1.teks)

    # Saat memanggil fungsi f2()
    f2()
    
    # Stelah memanggil fungsi f2()
    print(f1.teks)

f1()
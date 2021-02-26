# Decorator

print('==========Decorator==========')

# Decorator
def ubah_semua_karakter_menjadi_huruf_besar(fungsi):
    def ubah_huruf():
        f = fungsi()
        ubah = f.upper()
        return ubah
    
    return ubah_huruf

def teks():
    return 'hello world'

hasil = ubah_semua_karakter_menjadi_huruf_besar(teks)
print(hasil())

print('')

# # Cara kerja decorator
# def ucap_selamat_malam(fungsi): # <- Mengambil fungsi
#     def ucap():
#         print('Selamat Malam!')
#         fungsi() # <- Menambahakan fungsi
    
#     return ucap # <- Mengembalikan fungsi

# def ucap_selamat_beristirahat():
#     print('Selamat Beristirahat!')

# print('=====Sebelum decorator=====')
# ucap_selamat_beristirahat()

# print('\n=====Setelah decorator=====')
# ucapan = ucap_selamat_malam(ucap_selamat_beristirahat)
# ucapan()

# Cara memanggil decorator
def ucap_selamat_malam(fungsi):
    def ucap():
        print('Selamat Malam!')
        fungsi()
    
    return ucap

@ucap_selamat_malam
def ucap_selamat_beristirahat():
    print('Selamat Beristirahat!')

ucap_selamat_beristirahat()

# Cara di atas sama dengan cara di baswah ini
# ucapan = ucap_selamat_malam(ucap_selamat_beristirahat)
# ucapan()

print('')

# Menggunakan parameter untuk mengambil parameter fungsi
def hitung_pembagian(fungsi):
    def hitung(x, y):
        if x == 0 or y == 0:
            print('Nilai tidak boleh 0')
            return

        return fungsi(x, y)
    return hitung

@hitung_pembagian
def input_nilai(x, y):
    return (x / y)

hasil_pembagian = input_nilai
print(hasil_pembagian(5, 5))

print('')

# Mengambil sejumlah argumen menggunakan *args
def hitung_total_pendapatan_bersih(fungsi):
    def hitung(*args):
        total_pendapatan = fungsi(*args)
        pendapatan_bersih = total_pendapatan - 150000
        return pendapatan_bersih
    
    return hitung

@hitung_total_pendapatan_bersih
def hitung_total_pendapatan(*args):
    total = 0 
    for item in args:
        total = total + item
    
    return total

print(hitung_total_pendapatan(100000,100000,100000,100000,100000))

print('')

# Mengambil sejumlah argumen menggunakan *kwargs
def tambah_keterangan_informasi(fungsi):
    def ubah(**kwargs):
        print('=' * 10, 'Data Diri', '=' * 10 )
        fungsi(**kwargs)
    
    return ubah

@tambah_keterangan_informasi
def tampilkan_informasi(**kwargs):
    for key, value in kwargs.items():
        print(key, '=', value) 
    
tampilkan_informasi(Nama='dikyindrah', Umur=21, Alamat='Bandar Lampung')

print('')

# fungsi dapat didekorasi beberapa kali dengan dekorator 
# yang berbeda atau sama
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hello")

# Cara di atas sama dengan cara di baswah ini
# p = star(percent(printer))
# p('Hello')
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

# def ucap_selamat_malam(fungsi):
#     def ucap():
#         print('Selamat Malam!')
#         fungsi()
    
#     return ucap

# def ucap_selamat_beristirahat():
#     print('Selamat Beristirahat!')

# print('=====Sebelum decorator=====')
# ucap_selamat_beristirahat()

# print('\n=====Setelah decorator=====')
# ucapan = ucap_selamat_malam(ucap_selamat_beristirahat)
# ucapan()

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
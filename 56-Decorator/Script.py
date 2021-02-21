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



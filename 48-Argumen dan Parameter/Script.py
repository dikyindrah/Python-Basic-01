# Argumen dan parameter

print('==========Argumen dan Paramenter==========')

# Fungsi dengan parameter
def tampilkan_teks(teks):
    print(teks)

# Fungsi dengan parameter lebih dari satu
def data_diri(nama, umur, alamat):
    print('Nama   =', nama)
    print('Umur   =', umur)
    print('Alamat =', alamat)

# Fungsi dengan argumen kata kunci
def penjumlahan(x, y):
    hasil_penjumlahan = x + y
    print(hasil_penjumlahan)

# Fungsi dengan argumen default
def kirim_pesan(pesan='Maaf, anda belum menginputkan pesan!'):
    print(pesan)

# Fungsi dengan *args
def perkalian(*args):
    hasil_perkalian = 1
    for value in args:
        hasil_perkalian = hasil_perkalian * value
    
    print(hasil_perkalian)

# Fungsi dengan **kwargs
def minuman(**kwargs):
    for key, value in kwargs.items():
        print('%s = %s' %(key, value))

# Fungsi dengan parameter *args dan **kwargs
def hari(*args, **kwargs):
    for value in args:
        print(value)
    
    for key, value in kwargs.items():
        print('%s = %s' %(key, value))

# Panggil seluruh fungsi
tampilkan_teks('Hello World!')
print('')
data_diri('Diky Indra Hermawanto', 21, 'Bandar Lampung')
print('')
penjumlahan(y=5, x=10)
print('')
kirim_pesan()
print('')
perkalian(5, 6, 7, 8, 9, 1, 2)
print('')
minuman(Sprite=7000, Mizone=8500)
print('')

# Menggunakan *args dan **kwargs untuk memanggil fungsi data_diri()
args = ('Diky Indra Hermawanto', 21, 'Bandar Lampung')
data_diri(*args)

kwargs = {'nama':'Diky Indra Hermawanto', 'umur':21, 'alamat':'Bandar Lampung'}
data_diri(**kwargs)

print('')

# Menggunakan *args dan **kwargs di baris yang sama untuk 
# memanggil fungsi hari()
hari('senin', 'selasa', 
     'rabu', hari_ke_4='kamis', 
      hari_ke_5='jumat', hari_ke_6='sabtu', 
      hari_ke_7='minggu')

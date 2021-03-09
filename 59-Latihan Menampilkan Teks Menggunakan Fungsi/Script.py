# Latihan menampilkan teks menggunakan fungsi

# Fungsi
def tampil_teks(teks):
    print(teks)

def ulangi_teks(teks, jumlah):
    for i in range(jumlah):
        print(teks)

def tampil_teks_pada_list(list_teks):
    for item in list_teks:
        print(item)

def input_teks():
    input_teks = str(input('Masukan teks: '))
    return input_teks

def input_jumlah():
    input_jumlah = int(input('Masukan jumlah: '))
    return input_jumlah


# Memanggil fungsi
teks = input_teks()
tampil_teks(teks)

print('')

teks = input_teks()
jumlah = input_jumlah()
ulangi_teks(teks, jumlah)

print('')

list_teks = ['Python', 'Java', 'C++', 'Go', 'Ruby']
tampil_teks_pada_list(list_teks)


# Latihan menampilkan angka menggunakan fungsi

# Fungsi
def tampil_angka(angka):
    print(angka)

def ulangi_angka(angka, jumlah):
    for i in range(jumlah):
        print(angka)

def tampil_urutan_angka(awal, akhir):
    for i in range(awal, akhir+1):
        print(i)

def tampil_angka_pada_list(list_angka):
    for item in list_angka:
        print(item, end=' ')

def input_angka():
    input_angka = int(input('Masukan angka: '))
    return input_angka

def input_jumlah():
    input_jumlah = int(input('Masukan jumlah: '))
    return input_jumlah


# Memanggil fungsi
angka = input_angka()
tampil_angka(angka)

print('')

angka = input_angka()
jumlah = input_jumlah()
ulangi_angka(angka, jumlah)

print('')

awal = int(input('Masukan angka awal: '))
akhir = int(input('Masukan angka akhir: '))
tampil_urutan_angka(awal, akhir)

print('')

lsit_angka = [4, 5, 1, 2, 10]
tampil_angka_pada_list(lsit_angka)


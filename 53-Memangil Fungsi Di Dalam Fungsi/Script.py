# Memanggil fungsi didalam fungsi lain

print('==========Memangil Fungsi Di Dalam Fungsi==========')

angka = []

# Fungsi yang di panggil
def isi_list(list_item):
    # Isi list dengan angka 1 sampai 10
    for i in range(1, 10+1, 1):
        # Masukan setiap angka kedalam variabel list_item
        list_item.append(i)
    
    # Mengembalikan nilai pada list_item
    return list_item

# Fungsi yang memanggil
def tampilkan_isi_list():
    # Memanggil funsi isi_list() dan menyimpan nilainya 
    # kedalam variabel list_item
    list_item = isi_list(angka)

    # Menampilkan seluruh item pada list_item
    for item in list_item:
        print(item, end=' ')

# Memanggil fungsi tampilkan_isi_list()
tampilkan_isi_list()
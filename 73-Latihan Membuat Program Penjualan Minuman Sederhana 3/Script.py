from prettytable import PrettyTable

def main():
    nama_minuman = ['Sprite', 
                    'Coca-cola', 
                    'Mizone', 
                    'Pocari Sweat', 
                    'Teh Botol Sosro']

    harga_minuman = [7000, 
                    12000, 
                    7500, 
                    5000, 
                    6000, 
                    8500]

    daftar_minuman = buat_tabel()
    i = 0
    jumlah_minuman = len(nama_minuman)
    while i < jumlah_minuman:
        daftar_minuman.add_row([i+1, nama_minuman[i], harga_minuman[i]])
        i = i +1
    
    minuman_user = []
    pesan_minuman = True
    while pesan_minuman == True:
        print('\n\tDaftar Minuman')
        print(daftar_minuman)
        nomor_minuman = int(input(f'\nPilih minuman [1-{jumlah_minuman}]: '))
        minuman_user.append(nomor_minuman-1)
        pilihan = str(input('Lagi ? [y/t] : '))
        if pilihan.lower() == 'y':
            pesan_minuman = True
        else:
            pesan_minuman = False

    tampil_keterangan_pesanan(minuman_user, nama_minuman, harga_minuman)
    jumlah_pesanan = len(minuman_user)
    total_harga = hitung_total_harga(minuman_user, harga_minuman)
    print('\nJumlah Pesanan \t:', jumlah_pesanan)
    print('Total Harga \t:', total_harga)

    jumlah_uang = int(input('\nMasukan uang \t: '))
    if jumlah_uang >= total_harga:
        uang_kembalian = hitung_uang_kembalian(jumlah_uang, total_harga)
        tampil_keterangan_pesanan(minuman_user, nama_minuman, harga_minuman)
        print('\nJumlah Pesanan \t:', jumlah_pesanan)
        print('Total Harga \t:', total_harga)
        print('Jumlah Uang \t:', jumlah_uang)
        print('Kembalian \t:', uang_kembalian, '\n')
    else:
        print('Maaf, uang anda tidak cukup...\n')

def buat_tabel():
    tabel = PrettyTable()
    tabel.field_names = ['No', 'Nama Minuman', 'Harga']
    tabel.align['No'] = 'c'
    tabel.align['Nama Minuman'] = 'l'
    tabel.align['Harga'] = 'r'

    return tabel

def tampil_keterangan_pesanan(minuman_user, nama_minuman, harga_minuman):
    keterangan_pesanan = buat_tabel()

    jumlah_pesanan = len(minuman_user)
    i = 0
    while i < jumlah_pesanan:
        n = minuman_user[i]
        keterangan_pesanan.add_row([i+1, nama_minuman[n], harga_minuman[n]])
        i = i +1        
    
    print('\n     Keterangan Pesanan')    
    print(keterangan_pesanan)

def hitung_total_harga(minuman_user, harga_minuman):
    i = 0
    total_harga = 0
    jumlah_pesanan = len(minuman_user)
    while i < jumlah_pesanan:
        n = minuman_user[i]
        total_harga = total_harga + harga_minuman[n]
        i = i + 1
    
    return total_harga

def hitung_uang_kembalian(jumlah_uang, total_harga):
    uang_kembalian = jumlah_uang - total_harga
    return uang_kembalian

main()
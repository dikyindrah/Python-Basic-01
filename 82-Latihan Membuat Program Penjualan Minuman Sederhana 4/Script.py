from prettytable import PrettyTable

def main():    
    minuman = {'nama_minuman':{1:'Sprite', 2:'Coca-cola', 
                               3:'Mizone', 4:'Pocari Sweat', 
                               5:'Teh Botol Sosro'},
               'harga_minuman':{1:7000, 2:12000, 
                                3:7500, 4:5000, 
                                5:8500}}

    
    tabel_menu_minuman = buat_tabel()
    lenght = int((len(minuman['nama_minuman'])+len(minuman['harga_minuman']))/2)
    for i in range(1, lenght+1):
        tabel_menu_minuman.add_row([i, minuman['nama_minuman'][i], minuman['harga_minuman'][i]])

    minuman_user = {'nama_minuman':{}, 'harga_minuman':{}}
    pesan_minuman = True
    i = 1
    while pesan_minuman == True:
        print('\nDaftar Minuman')
        print(tabel_menu_minuman)
        no = int(input('Pilih minuman \t: '))
        minuman_user['nama_minuman'][i] = minuman['nama_minuman'][no]
        minuman_user['harga_minuman'][i] = minuman['harga_minuman'][no]
        pilihan = str(input('Lagi ? [y/t] \t: '))
        if pilihan.lower() == 'y':
            pesan_minuman = True
            i = i + 1
        else:
            pesan_minuman = False

    tabel_keterangan_pesanan = buat_tabel()
    i = 1
    jumlah_item = int((len(minuman_user['nama_minuman'])+len(minuman_user['harga_minuman']))/2)
    while i <= jumlah_item:
        tabel_keterangan_pesanan.add_row([i, minuman_user['nama_minuman'][i], minuman_user['harga_minuman'][i]])
        i = i + 1
    
    total_harga = hitung_total_harga(minuman_user, jumlah_item)
    print('\nKeterangan Pesanan')
    print(tabel_keterangan_pesanan)
    print('\nJumlah Item \t:',jumlah_item)
    print('Total Harga \t:',total_harga)

    jumlah_uang = int(input('\nMasukan uang \t: '))
    if jumlah_uang >= total_harga:
        print('\nKembalian \t:',hitung_uang_kembalian(jumlah_uang, total_harga))
    else:
        print('\nMaaf, uang anda tidak cukup.')
    
def buat_tabel():
    tabel = PrettyTable()
    tabel.field_names = ['No', 'Nama Minuman', 'Harga']
    tabel.align['No'] = 'c'
    tabel.align['Nama Minuman'] = 'l'
    tabel.align['Harga'] = 'r'

    return tabel

def hitung_total_harga(minuman_user, jumlah_item):
    total_harga = 0
    i = 1
    while i <= jumlah_item:
        total_harga = total_harga + minuman_user['harga_minuman'][i]
        i = i + 1
    return total_harga

def hitung_uang_kembalian(jumlah_uang, total_harga):
    return jumlah_uang - total_harga

main() 
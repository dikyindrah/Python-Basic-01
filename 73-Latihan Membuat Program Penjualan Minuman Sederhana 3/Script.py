# Latihan membuat program penjualan minuman sederhana 3
from prettytable import PrettyTable

def hitung_total_pembelian(minuman_user, harga_minuman):
        total_harga = 0
        for i in range(len(minuman_user)):
                nomor = minuman_user[i]
                total_harga = total_harga + harga_minuman[nomor]
        return total_harga

def hitung_uang_kembalian(jumlah_uang):
        total_harga_pembelian = hitung_total_pembelian(minuman_user, harga_minuman)
        if jumlah_uang < total_harga_pembelian:
                return 'Maaf, Uang anda tidak cukup.'
        else:
                return jumlah_uang - total_harga_pembelian

def keterangan_pembelian(minuman_user, harga_minuman, total_uang):
        total_pembelian = hitung_total_pembelian(minuman_user, harga_minuman)
        uang_kembalian = hitung_uang_kembalian(total_uang)
        tabel_keterangan_pembelian = PrettyTable()
        tabel_keterangan_pembelian.field_names = ['Nama Minuman', 'Harga']
        tabel_keterangan_pembelian.align['Nama Minuman'] = 'l'
        tabel_keterangan_pembelian.align['Harga'] = 'r'

        for i in range(len(minuman_user)):
                nomor = minuman_user[i]
                tabel_keterangan_pembelian.add_row(nama_minuman[nomor], harga_minuman[i])
        
        print(tabel_keterangan_pembelian)


def main():
        tabel_minuman = PrettyTable()
        tabel_minuman.field_names = ['No','Nama Minuman', 'Harga']
        tabel_minuman.align['No'] = 'c'
        tabel_minuman.align['Nama Minuman'] = 'l'
        tabel_minuman.align['Harga'] = 'r'

        jumlah_item = int(((len(nama_minuman) + len(harga_minuman))/2))
        i = 0
        while i < jumlah_item:
                tabel_minuman.add_row([i+1, nama_minuman[i], harga_minuman[i]])
                i = i + 1

        pesan_minuman = True
        while pesan_minuman == True:
                print('\n\tDaftar Minuman')
                print(tabel_minuman)
                nomor_minuman = int(input(f'\nSilahkan pilih minuman [input nomor 1 - {jumlah_item}]: '))
                jawaban_user = str(input('Apakah anda ingin memesan minuman lagi [y/t]: '))
                minuman_user.append(nomor_minuman-1)
                if jawaban_user == 'y':
                        pesan_minuman = True
                else:
                        pesan_minuman = False

        total_pembelian = hitung_total_pembelian(minuman_user, harga_minuman)
        print('total pembelian =', total_pembelian)
        total_uang = int(input('Silahkan masukan uang anda: '))
        uang_kembalian = hitung_uang_kembalian(total_uang)
        print('uang kembalian =', uang_kembalian)
        keterangan_pembelian(minuman_user, )

nama_minuman = ['Sprite', 
                'Coca-cola', 
                'Pocari Sweat',
                'Mizone',
                'Teh Botol Sosro']

harga_minuman = [7000, 
                 8500, 
                 5500, 
                 7500, 
                 6000]

minuman_user = []

main()

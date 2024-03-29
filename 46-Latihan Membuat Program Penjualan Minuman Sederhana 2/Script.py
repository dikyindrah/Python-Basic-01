# Program penjualan minuman 2
import os

print('\n==========Program Penjualan Minuman==========\n')

nama_minuman = ''
pesan_minuman = True
jumlah_uang, uang_kembalian, harga_minuman = 0, 0, 1

while pesan_minuman == True:
    print(''' 
            Daftar Minuman
    ------------------------------------
    No  |   Nama Minuman   |  Harga  
    -----+------------------+-----------
    1   |  Sprite          | Rp.7000,-
    2   |  Coca-cola       | Rp.8500,- 
    3   |  Pocari Sweat    | Rp.5500,-
    4   |  Mizone          | Rp.7500,-
    5   |  Teh Botol Sosro | Rp.6000,-
    ------------------------------------
    ''')
    nomor_minuman = str(input('Silahkan pilih minuman yang anda inginkan [Pilih nomor 1-5]: '))

    if nomor_minuman == '1':
        nama_minuman = 'Sprite'
        harga_minuman = 7000
    elif nomor_minuman == '2':
        nama_minuman = 'Coca-cola'
        harga_minuman = 8500
    elif nomor_minuman == '3':
        nama_minuman = 'Pocari Sweat'
        harga_minuman = 5500
    elif nomor_minuman == '4':
        nama_minuman = 'Mizone'
        harga_minuman = 7500
    elif nomor_minuman == '5':
        nama_minuman = 'Teh Botol Sosro'
        harga_minuman = 7500
    else:
        print('\nMaaf, minuman tidak tersedia!')

    if nomor_minuman.isdigit():
        if int(str(nomor_minuman)) <= 5:
            print('\nAnda memilih', nama_minuman, 'dengan harga Rp.', harga_minuman, ',-')
            jumlah_uang = int(input('\nMasukan jumlah uang anda: '))
            if jumlah_uang >= harga_minuman:
                uang_kembalian = jumlah_uang - harga_minuman
            else:
                print('Maaf, jumlah uang anda tidak cukup!')
    
    if nomor_minuman.isdigit():
        if int(str(nomor_minuman)) <= 5:
            if jumlah_uang >= harga_minuman:
                print('\n--------------------------------')
                print('      Keterangan Pembelian      ')
                print('--------------------------------')
                print(' Nama Minuman   =', nama_minuman)
                print(' harga Minuman  =', harga_minuman)
                print(' Jumlah Uang    =', jumlah_uang)
                print(' Uang Kembalian =', uang_kembalian)
                print('--------------------------------')
                print('\nTerimakasih!\n')
            else:
                print('\nTerimakasih!')

    jawaban_user = str(input('\nApakah anda ingin memesan minuman lagi [y/t]: '))
    if jawaban_user == 'y':
        pesan_minuman = True
        nama_minuman = ''
        harga_minuman = 0
        jumlah_uang = 0
        uang_kembalian = 0
        os.system('cls')
    else:
        pesan_minuman = False
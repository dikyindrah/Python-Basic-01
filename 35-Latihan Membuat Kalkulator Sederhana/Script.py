# Program kalkulator sederhana

print('\n==========Kalkulator Sederhana==========\n')

hasil_perhitungan = 0
nilai_1, nilai_2 = 0, 0

print('''
| Operasi Matematika |\n
1.  Penjumlahan
2.  Pengurangan
3.  Perkalian
4.  Pembagian
5.  Pembagian Bulat
6.  Sisa Bagi
7.  Perpangkatan
''')

operasi_matematika = str(input('Silahkan pilih operasi matematika yang di inginkan [1-7]: '))

if operasi_matematika == '1':
    print('\n| Penjumlahan |')
    nilai_1 = int(input('\nMasukan nilai 1: '))
    nilai_2 = int(input('Masukan nilai 2: '))
    hasil_perhitungan = nilai_1 + nilai_2
    print(nilai_1, '+', nilai_2, '=', hasil_perhitungan)
elif operasi_matematika == '2':
    print('\n| Pengurangan |')    
    nilai_1 = int(input('\nMasukan nilai 1: '))
    nilai_2 = int(input('Masukan nilai 2: '))
    hasil_perhitungan = nilai_1 - nilai_2  
    print(nilai_1, '-', nilai_2, '=', hasil_perhitungan)    
elif operasi_matematika == '3':
    print('\n| Perkalian |')
    nilai_1 = int(input('\nMasukan nilai 1: '))
    nilai_2 = int(input('Masukan nilai 2: '))
    hasil_perhitungan = nilai_1 * nilai_2  
    print(nilai_1, '*', nilai_2, '=', hasil_perhitungan)       
elif operasi_matematika == '4':
    print('\n| Pembagian |')
    nilai_1 = int(input('\nMasukan nilai 1: '))
    nilai_2 = int(input('Masukan nilai 2: '))
    hasil_perhitungan = nilai_1 / nilai_2
    print(nilai_1, '/', nilai_2, '=', hasil_perhitungan)   
elif operasi_matematika == '5':
    print('\n| Pembagian Bulat |')
    nilai_1 = int(input('\nMasukan nilai 1: '))
    nilai_2 = int(input('Masukan nilai 2: '))
    hasil_perhitungan = nilai_1 // nilai_2
    print(nilai_1, '//', nilai_2, '=', hasil_perhitungan)   
elif operasi_matematika == '6':
    print('\n| Sisa Bagi |')
    nilai_1 = int(input('\nMasukan nilai 1: '))
    nilai_2 = int(input('Masukan nilai 2: '))
    hasil_perhitungan = nilai_1 % nilai_2
    print(nilai_1, '%', nilai_2, '=', hasil_perhitungan)   
elif operasi_matematika == '7':
    print('\n| Perpangkatan |')
    nilai_1 = int(input('\nMasukan nilai 1: '))
    nilai_2 = int(input('Masukan nilai 2: '))
    hasil_perhitungan = nilai_1 ** nilai_2
    print(nilai_1, '**', nilai_2, '=', hasil_perhitungan)   
else:
    print('Operasi matematika yang anda pilih tidak sesuai!')

print('\n')

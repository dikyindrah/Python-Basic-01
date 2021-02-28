# Fungsi rekursif

print('==========Fungsi Rekursif==========\n')

# # Contoh fungsi rekursif
# def test_rekursif():
#     # Pernyataan
#     print('Ini adalah pernyataan yang di ulang menggunakan fungsi rekursif')
    
#     # Memanggil perulangan di dalam blok fungsinya sendiri
#     test_rekursif()

# # Memanggil fungsi
# test_rekursif()

print('')

# Fungsi rekursif dengan control flow
def ulang_sebanyak_n(start, stop):
    if start < stop+1:
        print(start)
        start = start + 1
        ulang_sebanyak_n(start, stop)
    

start = int(input('start : '))
stop = int(input('stop  : '))
ulang_sebanyak_n(start, stop)

print('')

# Mencari nilai faktorial dengan fungsi rekursif
def faktorial(x):
    if x == 1:
        return 1
    else:
        return (x * faktorial(x-1))

nilai = 4
print(faktorial(nilai))

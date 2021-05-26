# Mengakses karakter pada string

print('==Mengakses Karakter Pada String=====')
teks = 'python'
print('teks =',teks,'\ntype =',type(teks),'\nlen = ',len(teks))

print('\n==Mengakses Karakter Pada String Dengan Indeks Positif=====')
# Karakter pertama
print('teks[0] =',teks[0])
# Karakter terakhir
print('teks[5] =',teks[5])

print('\n==Mengakses Karakter Pada String Dengan Indeks Negatif=====')
# Karakter terakhir
print('teks[-1] =',teks[-1])
# Karakter pertama
print('teks[-6] =',teks[-6])

print('\n==Memotong Karakter Pada String=====')
print('teks[1:2]',teks[1:2])
print('teks[2:5]',teks[2:5])
print('teks[-1:-4] =',teks[1:-2])
print('teks[-1:-4] =',teks[2:-1])

print('\n==Mengakses Karakter Pada String Diluar Rentang Indeks dan Angka Selain Integer=====')
# Diluar rentang indeks 0-5
print('teks[15] =',teks[15])
print('teks[-8] =',teks[-8])

# Indeks selain integer
print('teks[1.5] =',teks[1.5])
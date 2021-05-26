# String special operators
print('=====String Special Operators=====')

print('\n==Menggabungkan String=====')

# Cara pertama
teks1 = 'Saya sedang'
teks2 = ' belajar python'
print(teks1+teks2)

# Cara kedua
print('Selamat'+' malam')

# Cara ketiga
teks3 = 'Ini adalah' + ' hari senin'
print(teks3)

print('\n==Menggandakan String=====')
# Cara pertama
print('Hello World '*5)

# Cara kedua
teks = 'python '
print(teks*10)

print('==Mengakses Karakter Pada String=====')
teks = 'python'
print('teks =',teks,'\ntype =',type(teks),'\nlen = ',len(teks))

# Mengakses Karakter Pada String Dengan Indeks Positif
# Karakter pertama
print('teks[0] =',teks[0])
# Karakter terakhir
print('teks[5] =',teks[5])

# Mengakses Karakter Pada String Dengan Indeks Negatif
# Karakter terakhir
print('teks[-1] =',teks[-1])
# Karakter pertama
print('teks[-6] =',teks[-6])

print('\n==Mengakses Karakter Pada String Dengan Rentang Tertentu=====')
print('teks[1:2]',teks[1:2])
print('teks[2:5]',teks[2:5])
print('teks[-1:-4] =',teks[1:-2])
print('teks[-1:-4] =',teks[2:-1])

print('\n==Memeriksa Karater Pada String=====')
teks = 'python'
print('teks =',teks)

# Memeriksa apakah ada karakter x pada string
print('p' in teks)
print('h' in teks)
print('k' in teks)

# Memeriksa apakah tidak ada karakter x pada string
print('k' not in teks)
print('y' not in teks)
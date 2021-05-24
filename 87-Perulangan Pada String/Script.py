# Perulangan pada string

print('=====Perulangan Pada String=====')

teks = 'helloworld'
print('teks =',teks)
hitung = 0
for i in range(len(teks)):
    if 'l' == teks[i]:
        hitung = hitung + 1

print('jumlah l pada teks',teks,'adalah',hitung)
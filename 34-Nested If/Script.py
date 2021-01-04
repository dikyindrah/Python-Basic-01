# Nested If

print('\n==========Nested If==========\n')

angka = int(input('Masukan angka: '))

if angka != 0:
    if angka % 2 == 1:
        print(angka, 'bilangan ganjil')
    else:
        print(angka, 'bilangan genap')
else:
    print('Anda harus memasukan angka!')



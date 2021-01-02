# Program kalkulator sederhana

print('\n==========Kalkulator Sederhana==========\n')

x = int(input('Masukan nilai x: '))
y = int(input('Masukan nilai y: '))

print('\n| Penjumlahan      | ', x, '+', y, '  = ', (x+y))
print('| Pengurangan      | ', x, '-', y, '  = ', (x-y))
print('| Pembagian        | ', x, '/', y, '  = ', (x/y))
print('| Pembagian Bulat  | ', x, '//', y, ' = ', (x//y))
print('| Sisa Bagi        | ', x, '%', y, '  = ', (x%y))
print('| Perpangkatan     | ', x, '**', y, ' = ', (x**y))
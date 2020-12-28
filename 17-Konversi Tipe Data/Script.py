# Konversi tipe data

print('\n==========Konversi Tipe Data Implisit==========\n')
print('Contoh 1:\n')
num_int = 123
num_flo = 1.23

# Proses konversi dilakukan disini
num_new = num_int + num_flo

print("Tipe data dari num_int:",type(num_int))
print("Tipe data dari num_flo:",type(num_flo))

print("Nilai dari num_new:", num_new)
print("Tipe data dari num_new:",type(num_new))

print('\nContoh 2:\n')
num_int = 123
num_str = "456"

print("Tipe data dari num_int:", type(num_int))
print("Tipe data dari num_str:", type(num_str))

# Proses konversi dilakukan disini
# print(num_int+num_str)


print('\n==========Konversi Tipe Data Eksplisit==========\n')
print('Contoh 1:\n')
num_int = 123
num_str = "456"

print("Tipe data dari num_int:", type(num_int))
print("Tipe data dari num_str sebelum Type Casting:", type(num_str))

num_str = int(num_str)
print("Tipe data dari num_str setelah Type Casting:", type(num_str))

num_sum = num_int + num_str

print("Jumlah num_int dan num_str:", num_sum)
print("Tipe data dari hasil penjulmalahan:", type(num_sum))

print('\nContoh 2:\n')
print('Konversi Tipe Data Ke Integer:\n')
num_str = '25'
num_int = int(num_str)
print('Data dan Tipe Data sebelum dikonversi:', num_str, type(num_str))
print('Data dan Tipe Data setelah dikonversi:', num_int, type(num_int))

print('\nKonversi Tipe Data Ke Float :\n')
num_int = 48
num_flo = float(num_int)
print('Data dan Tipe Data sebelum dikonversi:', num_int, type(num_int))
print('Data dan Tipe Data setelah dikonversi:', num_flo, type(num_flo))

print('\nKonversi Tipe Data Integer Ke Biner:\n')
num_int = 56
num_bin = bin(num_int)
print('Data dan Tipe Data sebelum dikonversi:', num_int, type(num_int))
print('Data dan Tipe Data setelah dikonversi:', num_bin, type(num_bin))

print('\nKonversi Tipe Dat Integer Ke Oktal:\n')
num_int = 12
num_okt = oct(num_int)
print('Data dan Tipe Data sebelum dikonversi:', num_int, type(num_int))
print('Data dan Tipe Data setelah dikonversi:', num_okt, type(num_okt))

print('\nKonversi Tipe Data Integer Ke Heksadesimal:\n')
num_int = 12
num_hex = hex(num_int)
print('Data dan Tipe Data sebelum dikonversi:', num_int, type(num_int))
print('Data dan Tipe Data setelah dikonversi:', num_hex, type(num_hex))

print('\nKonversi Tipe Data Integer Ke Comoplex:\n')
num_x = 2
num_y = 4
num_com = complex(num_x, num_y)
print('Data dan Tipe Data sebelum dikonversi:', num_x, type(num_x), num_y, type(num_y))
print('Data dan Tipe Data setelah dikonversi:', num_com, type(num_com))

print('\nKonversi Tipe Data Integer Ke Character (ASCII):\n')
num_int = 190
num_chr = chr(num_int)
print('Data dan Tipe Data sebelum dikonversi:', num_int, type(num_int))
print('Data dan Tipe Data setelah dikonversi:', num_chr, type(num_chr))

print('\nKonversi Tipe Data Character (ASCII) Ke Integer:\n')
num_str = 'R'
num_ord = ord(num_str)
print('Data dan Tipe Data sebelum dikonversi:', num_str, type(num_str))
print('Data dan Tipe Data setelah dikonversi:', num_ord, type(num_ord))

print('Konversi Tipe Data Ke List:\n')
num_str = 'diky'
num_list = list(num_str)
print('Data dan Tipe Data sebelum dikonversi:', num_str, type(num_str))
print('Data dan Tipe Data setelah dikonversi:', num_list, type(num_list))

print('Konversi Tipe Data Ke Tuple:\n')
num_str = 'diky'
num_tuple = tuple(num_str)
print('Data dan Tipe Data sebelum dikonversi:', num_str, type(num_str))
print('Data dan Tipe Data setelah dikonversi:', num_tuple, type(num_tuple))

print('Konversi Tipe Data Ke Set:\n')
num_str = 'diky'
num_set = set(num_str)
print('Data dan Tipe Data sebelum dikonversi:', num_str, type(num_str))
print('Data dan Tipe Data setelah dikonversi:', num_set, type(num_set))

print('Konversi Tipe Data Ke Dictionary:\n')
num_tuple = ((1, 'a'), (2, 'b'), (3, 'c'))
num_dict = dict(num_tuple)
print('Data dan Tipe Data sebelum dikonversi:', num_tuple, type(num_tuple))
print('Data dan Tipe Data setelah dikonversi:', num_dict, type(num_dict))

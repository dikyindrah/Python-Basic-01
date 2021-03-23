# Konversi tipe data berurut

print('\n==========Konversi Tipe Data Berurut==========')
print('\n==Konversi List ke Tuple=====\n')
# Sebelum dikonversi
list_a = [10, 20, 30, 40, 50]
print(list_a, type(list_a))

# Setelah dikonversi
tuple_a = tuple(list_a)
print(tuple_a, type(tuple_a))

print('\n==Konversi Tuple ke List=====\n')
# Sebelum dikonversi
tuple_b = ('aku', 'sedang', 'belajar', 'python')
print(tuple_b, type(tuple_b))

# Setelah dikonversi
list_b = list(tuple_b)
print(list_b, type(list_b))

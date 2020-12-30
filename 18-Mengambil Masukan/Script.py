# Mengambil masukan

print('\n==========Mengambil Masukan==========')

print('Menggunakan fungsi input():\n')
data = input('Masukan data: ')
print(data)
print(type(data))

print('\n\nMenggunakan fungsi input() dan Type Casting:\n')
print('Integer')
data = int(input('Masukan data: '))
print(data)
print(type(data))

print('\n\nFloat')
data = float(input('Masukan data: '))
print(data)
print(type(data))

print('\n\nString')
data = str(input('Masukan data: '))
print(data)
print(type(data))

print('\n\nBoolean')
data = bool(int(input('Masukan data: ')))
print(data)
print(type(data))
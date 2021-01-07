# For

print('\n==========For==========\n')

print('\n| Tampilkan 5 angka |\n')
for i in range(5):
    print(i)

print('\n| Tampilkan angka 1 sampai 5 |\n')
for i in range(1, 5+1):
    print(i)

print('\n| Tampilkan 5 angka secara ascending |\n')
for i in range(0, 5, 1):
    print(i)

print('\n| Tampilkan 5 angka secara descending |\n')
for i in range(5, 0, -1):
    print(i)

list_hari = [
    'Senin', 
    'Selasa', 
    'Rabu', 
    'Kamis', 
    'Jumat', 
    'Sabtu', 
    'Minggu'
]

print('\n| Tampilkan seluruh item pada list |\n')
for hari in list_hari:
    print(hari)

print('\n| Tampilkan seluruh item pada list berdasarkan indeks |\n')
for hari in range(len(list_hari)):
    print('Indeks ke', hari, 'adalah hari', list_hari[hari])
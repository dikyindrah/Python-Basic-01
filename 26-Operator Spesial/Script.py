# Operator spesial

print('\n==========Operator Spesial==========')

print('\nOperator Identitas\n')
x = 5
y = 5
print('Nilai x =', x)
print('Nilai y =', y)
print('\n| is     |')
print('x is y     =', (x is y))
print('\n| is not |')
print('x not is y =', (x is not y))

x = 8
y = 25

print('\n\nNilai x =', x)
print('Nilai y =', y)
print('\n| is     |')
print('x is y     =', (x is y))
print('\n| is not |')
print('x is not y =', (x is not y))

print('\nOperator Keanggotaan\n')

nama = 'Diky Indra Hermawanto'
hari = [
    'Senin', 
    'Selasa', 
    'Rabu', 
    'Kamis', 
    'Jumat', 
    'Sabtu', 
    'Minggu'
]

print('nama =',nama)
print('\n| in     |')
print('Diky not in nama  =', 'Diky' in nama)
print('Indra in nama =', 'Indra' in nama)
print('indra in nama =', 'indra' in nama)
print('Riky in nama  =', 'Riky' in nama)

print('\n| not in |')
print('Diky not in nama  =', 'Diky' not in nama)
print('Indra not in nama =', 'Indra' not in nama)
print('indra not in nama =', 'indra' not in nama)
print('Riky not in nama  =', 'Riky' not in nama)

print('\nhari =', hari)
print('\n| in     |')
print('Senin in hari  =', 'Senin' in hari)
print('Selsa in hari  =', 'Selasa' in hari)
print('Natal in hari  =', 'Natal' in hari)
print('minggu in hari =', 'minggu' in hari)

print('\n| not in |')
print('Senin not in hari  =', 'Senin' not in hari)
print('Selsa not in hari  =', 'Selasa' not in hari)
print('Natal not in hari  =', 'Natal' not in hari)
print('minggu not in hari =', 'minggu' not in hari)
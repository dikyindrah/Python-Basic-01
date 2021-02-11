# Ternary operator

print('==========Ternary Operator==========')

a = 10
b = 20

# Ternary operator if
hasil = 'a lebih kecil dari b' if a < b else 'a lebih besar dari b'
print(hasil)

'''
# Nested if
if a == b:
    print('a sama dengan b')
else:
    if a < b:
        print('a lebih kecil dari b')
    else:
        print('a lebih besar dari b')
'''

# Ternary operator nested if
hasil = 'a sama dengan b' if a == b else 'a lebih kecil dari b' if a < b else 'a lebih besar dari b'
print(hasil)

# Seleksi item pada tuple menggunakan ternary operator
hasil = (b, a) [a < b]
print(hasil)

# Seleksi item pada dictonary menggunakan ternary operator
hasil = {True:a, False:b} [a < b]
print(hasil)
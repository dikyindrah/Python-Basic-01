# Operator bitwise

print('\n==========Operator Bitwise==========\n')

x = 2
y = 5

print('\n|  &  |')
z = x & y
print('Nilai:', x, ', Binary:', format(x,'08b'))
print('Nilai:', y, ', Binary:', format(y,'08b'))
print('----------------------------(&)')
print('Nilai:', z, ', Binary:', format(z,'08b'))

print('\n|  |  |')
z = x | y
print('Nilai:', x, ', Binary:', format(x,'08b'))
print('Nilai:', y, ', Binary:', format(y,'08b'))
print('----------------------------(|)')
print('Nilai:', z, ', Binary:', format(z,'08b'))

print('\n|  ~  |')
z = ~x
print('Nilai: ', x, ', Binary:', format(x,'08b'))
print('----------------------------(~)')
print('Nilai:', z, ', Binary:', format(z,'08b'))

print('\n|  ^  |')
z = x ^ y
print('Nilai:', x, ', Binary:', format(x,'08b'))
print('Nilai:', y, ', Binary:', format(y,'08b'))
print('----------------------------(^)')
print('Nilai:', z, ', Binary:', format(z,'08b'))

print('\n|  >>  |')
z = x >> 1
print('Nilai:', x, ', Binary:', format(x,'08b'))
print('----------------------------(>>)')
print('Nilai:', z, ', Binary:', format(z,'08b'))

print('\n|  <<  |')
z = x << 1
print('Nilai:', x, ', Binary:', format(x,'08b'))
print('----------------------------(<<)')
print('Nilai:', z, ', Binary:', format(z,'08b'))
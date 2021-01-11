# Pernyataan kontrol loop

print('\n==========Pernyataan Kontrol loop==========')

print('|\n Break |\n')

for i in range(1, 10+1):
    print(i)
    if i == 5:
        break

print('\n| Continue |\n')

for i in range(1, 5+1):
    if i == 3:
        continue
    print(i)

print('\n| Pass |\n')

for i in range(1, 5+1):
    pass

print('\n| Else |\n')

for i in range(2, 2):
    print(i)
else:
    print('Argumen start pada fungsi range() harus lebih besar dari argumen stop')
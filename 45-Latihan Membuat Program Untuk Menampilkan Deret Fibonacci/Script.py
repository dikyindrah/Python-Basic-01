# Program untuk menampilkan deret fibonacci

print('\n==========Deret Fibonacci==========\n')

x = 0
y = 1
tmp = 0

for i in range(10):
    print(x, end=' ')
    tmp = x + y
    x = y
    y = tmp

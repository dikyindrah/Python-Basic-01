# Program untuk menampilkan deret bilangan prima

print('\n==========Deret Blangan Prima==========\n')

# Cara pertama
for i in range(2, 10):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=' ')

print('\n')

# Cara kedua
for i in range(2, 10):
    prima = True
    for j in range(2, i):
        if i % j == 0:
            prima = False   

    if prima == True:
        print(i, end=' ') 

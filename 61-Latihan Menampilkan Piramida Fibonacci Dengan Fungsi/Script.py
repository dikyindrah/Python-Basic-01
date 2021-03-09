# Latihan menampilkan deret fibonacci dengan fungsi

# Fungsi
def fibonacci(jumlah):
    x = 0
    y = 1
    tmp = 0
    list_fibonacci = []

    for i in range(jumlah):
        list_fibonacci.append(x)
        tmp = x + y
        x = y
        y = tmp
    
    return list_fibonacci

def tampil_piramida_fibonacci(list_fibonacci):
    panjang = len(list_fibonacci)

    for x in range(panjang):
        print('')
        for y in range(x):
            print(list_fibonacci[y], end=' ')

# Memanggil fungsi
tampil_piramida_fibonacci(fibonacci(10+1))
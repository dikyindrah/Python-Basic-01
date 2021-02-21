# Clousure

print('==========Clousure==========')

# Fungsi bersarang dengan closure
def hitung():
    nilai = 0
    def tambah():
        nonlocal nilai
        nilai = nilai + 1
        return nilai
    
    return tambah

hasil_hitung = hitung()

print(hasil_hitung())
print(hasil_hitung())
print(hasil_hitung())

print('')

# Fungsi bersarang biasa
def hitung():
    nilai = 0
    def tambah():
        nonlocal nilai
        nilai = nilai + 1
        return nilai
    
    print(tambah())

hitung()
hitung()
hitung()

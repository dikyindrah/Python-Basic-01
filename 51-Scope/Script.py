# Scope

print('==========Scope==========\n')

# Local
def cetak_angka():
    angka_pertama = 1
    print(angka_pertama)

cetak_angka()
# Variabel angka_pertama tidak bisa kita akses di luar fungsi
# angka_pertama

# Enclosing
def fungsi_bagian_luar():
    angka_pertama = 1
    def fungsi_bagian_dalam():
        angka_kedua = 2
        print(angka_pertama)
        print(angka_kedua)

    fungsi_bagian_dalam()
    print(angka_pertama)
    # Variabel angka_kedua tidak bisa diakses di luar fungsi bagian dalam
    # print(angka_kedua)

fungsi_bagian_luar()

# Global
list_hari = ['Senin', 'Selasa', 'Rabu', 
             'Kamis', 'Jumat', 'Sabtu', 
             'Minggu']

def tampilkan_seluruh_hari():
    for hari in list_hari:
        print(hari)

tampilkan_seluruh_hari()

# Built-in
list_angka = [3, 4, 6, 1]

print(len(list_angka))
print(min(list_angka))
print(max(list_angka))
print(sum(list_angka))
print(sorted(list_angka))
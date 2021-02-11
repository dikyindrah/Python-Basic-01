# Literal

print('==========Literal==========\n')

# String literal
print('==========String Literal==========')
# Kutip tunggal 
string_literal_kutip_tunggal = 'Diky Indra Hermawanto'
  
# Kutip ganda
string_literal_kutip_ganda = "Diky Indra Hermawanto"
  
# String multi baris
string_literal_multi_baris = '''
Diky  
    Indra  
         Hermawanto
'''

# String unicode
string_literal_unicode = u"\u00dcnic\u00f6de"

print(string_literal_kutip_tunggal)
print(string_literal_kutip_ganda)
print(string_literal_multi_baris)


# Numerik literal
print('==========Numerik Literal==========')

# Integer Literal

# Literal Binary
a = 0b1010 

# Literal Desimal
b = 100 

# Literal Oktal
c = 0o310 

# Literal Hexadesimal
d = 0x12c 

print(a, b, c, d)


# Float Literal
float_1 = 10.5
float_2 = 1.5e2

print(float_1, float_2)


# Complex Literal
x = 3.14j

print(x, x.imag, x.real)


# Boolean literal
print('\n==========Boolean Literal==========')

a = (1 == True) 
b = (1 == False) 
c = True + 3
d = False + 7

print("a is", a) 
print("b is", b) 
print("c:", c) 
print("d:", d) 


# Literal Koleksi
print('\n==========Literal Koleksi==========')

# List
buah = ["apel", "mangga", "jeruk"] 

# Tuple
angka  = (1, 2, 3) 

# Set
konsonan = {'a', 'e', 'i' , 'o', 'u'} 

# Dictionary
kamus = {'a':'apel', 'b':'belimbing', 'c':'cempedak'} 

print(type(buah),':', buah)
print(type(angka),':', angka)
print(type(konsonan),':', konsonan)
print(type(kamus),':', kamus)


# Spesial literal
print('\n==========Spesial Literal==========')

minuman = "Tersedia"
makanan = None

print(minuman)
print(makanan)

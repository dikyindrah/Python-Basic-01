# Program konversi suhu

print('\n==========Program Konversi Suhu==========\n')

celcius = float(input('Input suhu dalam celcius: '))

print('\nCelcius ke Reamur     =', ((4/5) * celcius), 'R')
print('Celcius ke Fahrenheit =', (((9/5) * celcius) + 32), 'F')
print('Celcius ke Kelvin     =', (celcius + 273), 'K')

reamur = float(input('\nInput suhu dalam reaamur: '))

print('\nReamur ke Celcius    =', ((5/4) * reamur), 'C')
print('Reamur ke Fahrenheit =', (((9/4) * reamur) + 32), 'F')
print('Reamur ke Kelvin     =', (((5/4) * reamur) + 273), 'K')

fahrenheit = float(input('\nInput suhu dalam fahrenheit: '))

print('\nFahrenheit ke Celcius    =', ((5/9) * (fahrenheit - 32)), 'C')
print('Fahrenheit ke Reamur     =', (((4/9) * (fahrenheit - 32))), 'R')
print('Fahrenheit ke Kelvin     =', ((fahrenheit - 32) * (5/9) + 273), 'K')

kelvin = float(input('\nInput suhu dalam kelvin: '))

print('\nKelvin ke Celcius    =', (kelvin - 273), 'C')
print('Kelvin ke Fahrenheit =', ((((kelvin - 273) * (9/5) + 32))), 'F')
print('Kelvin ke Reamur     =', ((4/5) * (kelvin - 273)), 'R')

# Operasi matematika pada set dan dictionary

print('\n==========Operasi Matematika Pada Set dan Dictionary==========')

dictionary_integerA = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}
dictionary_integerB = {'f':60, 'g':70, 'h':80, 'i':90, 'j':100}
dictionary_integerC = {}

print('\n==Menghitung Value Pada Satu Dictionary=====')
tmp = 0
for value in dictionary_integerA.values():
    tmp = tmp + value
print('total nilai:',tmp)

tmp = 0
for value in dictionary_integerB.values():
    tmp = tmp + value
print('total nilai:',tmp)

print('\n==Menghitung Value Pada Dua Dictionary=====')
list_keyA = list(dictionary_integerA.keys())
list_keyB = list(dictionary_integerB.keys())
length = int((len(dictionary_integerA) + len(dictionary_integerB)) / 2)

tmp = 0
for i in range(5):
    tmp = dictionary_integerA[list_keyA[i]] + dictionary_integerB[list_keyB[i]]
    dictionary_integerC.update({i:tmp})

print('dictionary_integerC', dictionary_integerC) 

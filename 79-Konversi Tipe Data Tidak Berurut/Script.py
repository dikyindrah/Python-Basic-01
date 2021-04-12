# Konversi tipe data tidak berurut
import itertools

print('\n==========Konversi Tipe Data Tidak Berurut==========')
print('\n==Set Ke Dictionary=====')
# Cara 1
set_item = {(1,'aku'), (2,'sedang'), (3,'belajar'), (4,'python')}
print(set_item)

dict_item = dict(set_item)
print(dict_item)

# Cara 2
set_key = {'a', 'b', 'c', 'd', 'e'}
set_value = {'apel', 'jeruk', 'mangga', 'anggur', 'durian'}

dict_item = itertools.zip_longest(set_key, set_value, fillvalue=None)
print(dict(dict_item))

# print('\n==Dictionary ke Set=====')
dict_item = {1:'aku', 2:'sedang', 3:'belajar', 4:'python'}
print(dict_item)

set_item = set(dict_item.items())
print(set_item)


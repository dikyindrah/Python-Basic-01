# Operasi matematika pada set dan dictionary bersarang
print('\n==========Operasi Matematika Pada Set dan Dictionary Bersarang==========')

print('\n==Operasi Matematika Pada Dictionary Bersarang=====')

# Cara pertama
dict_item = {'nilaiA':{'a':10,'b':20,'c':30},
             'nilaiB':{'a':40,'b':50,'c':60}}

list_nilaiA = []
list_nilaiB = []
list_item = []
for key, value in dict_item.items():
    if key != 'nilaiB':
        for key in value.keys():
            list_nilaiA.append(value[key])
    else:
        for key in value.keys():
            list_nilaiB.append(value[key])

        for i in range(len(list_nilaiA)):
            tmp = list_nilaiA[i] + list_nilaiB[i]
            list_item.append(tmp)
print(list_item) 

# Cara kedua
dict_a = {'nilaiA':{'a':100,'b':200,'c':300}}
dict_b = {'nilaiB':{'a':400,'b':500,'c':600}}

list_item_dict_a = []
for key, value in dict_a.items():
    for key in value.keys():
        list_item_dict_a.append(value[key])

list_item_dict_b = []
for key, value in dict_b.items():
    for key in value.keys():
        list_item_dict_b.append(value[key])

list_item = []
for i in range(int((len(list_item_dict_a)+len(list_item_dict_b))/2)):
    tmp = list_item_dict_a[i] + list_item_dict_b[i]
    list_item.append(tmp)
print(list_item)
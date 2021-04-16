minuman = {'nama_minuman':{1:'Sprite', 2:'Coca-cola', 
                           3:'Mizone', 4:'Pocari Sweat', 
                           5:'Teh Botol Sosro'},
            'harga_minuman':{1:7000, 2:12000, 
                             3:7500, 4:5000, 
                             5:8500}}

minuman_user = {'nama_minuman':{},
                'harga_minuman':{}}

minuman_user['nama_minuman'][1] = minuman['nama_minuman'][1]
minuman_user['harga_minuman'][1] = minuman['harga_minuman'][1]

print(minuman_user)
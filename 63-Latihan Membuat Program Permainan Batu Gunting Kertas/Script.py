# latihan membuat program permainan batu gunting kertas
import random

def komputer(pilihan):
    pilihan_komputer = random.choice(pilihan)
    return pilihan_komputer

def permainan(user, komputer, pilihan):
    status_permainan = ''

    if user.lower()=='batu' and komputer.lower()=='kertas':
        status_permainan = 'Menang'
    elif user.lower()=='batu' and komputer.lower()=='gunting':
        status_permainan = 'Menang'
    elif user.lower()=='batu' and komputer.lower()=='batu':
        status_permainan = 'Seri'
    elif user.lower()=='gunting' and komputer.lower()=='kertas':
        status_permainan = 'Menang'
    elif user.lower()=='gunting' and komputer.lower()=='batu':
        status_permainan = 'Kalah'
    elif user.lower()=='gunting' and komputer.lower()=='gunting':
        status_permainan = 'Seri'
    elif user.lower()=='kertas' and komputer.lower()=='gunting':
        status_permainan = 'Kalah'
    elif user.lower()=='kertas' and komputer.lower()=='kertas':
        status_permainan = 'Seri'
    else:
        status_permainan = ''
    
    return status_permainan

def status_permainan(user, komputer, pilihan):
    ada = False
    for item in pilihan:
        if pilihan_user == item:
            ada = True
            break
        else:
            ada = False

    if ada == True:
        status_permainan = permainan(pilihan_user, pilihan_komputer, pilihan)
        print('\nKamu Memilih   \t\t:', pilihan_user)
        print('Komputer Memilih \t:', pilihan_komputer)
        print('\n=====STATUS PERMAINAN=====')
        print('\tKamu', status_permainan, '\n')
    else:
        print('\nEROR\n')

pilihan = ['batu', 'gunting', 'kertas']

print('\n=====PERMAINAN BATU GUNTING KERTAS=====')
pilihan_user = str(input('Pilihan \t\t: '))
pilihan_komputer = komputer(pilihan)
status_permainan(pilihan_user, pilihan_komputer, pilihan)




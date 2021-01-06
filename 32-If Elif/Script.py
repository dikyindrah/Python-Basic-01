# If Elif

print('\n==========If Elif==========\n')

huruf_mutu = ''

print('\n|Input data siswa|')
nama_siswa = str(input('\nMasukan nama siswa     = '))
mata_pelajaran = str(input('Masukan mata pelajaran = '))
nilai_siswa = int(input('Masukan nilai siswa    = '))

if nilai_siswa >= 90 and nilai_siswa <= 100:
    huruf_mutu = 'A'
elif nilai_siswa >= 80 and nilai_siswa <= 89:
    huruf_mutu = 'B'
elif nilai_siswa >= 70 and nilai_siswa <= 79:
    huruf_mutu = 'C'
elif nilai_siswa >= 60 and nilai_siswa <= 69:
    huruf_mutu = 'D'
else:
    huruf_mutu = 'E'

print('\n\n|Hasil yang diperoleh siswa|')
print('\nNama Siswa     =', nama_siswa)
print('Nilai Siswa    =', nilai_siswa)
print('Mata Pelajaran =', mata_pelajaran)
print('Huruf Mutu     =', huruf_mutu)
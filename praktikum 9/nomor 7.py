mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('='*70)
print('NIM'.ljust(10),'NAMA MAHASISWA'.ljust(20),'TGL LAHIR'.ljust(15),'TEMPAT LAHIR')
print('-'*70)
for data in mhs :
    data = data.split(':')
    nim = data[0]
    nama = data[1]
    tgl = data [2]
    tgllahir = tgl.split('-')
    tanggal = tgllahir[2]
    bulan = tgllahir[1]
    tahun = tgllahir[0]
    tmpt = data [3]
    print(nim.ljust(10), nama.ljust(20), tanggal,'/', bulan,'/', tahun.ljust(5), tmpt)

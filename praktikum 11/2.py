from datetime import*

myfile = open('d:\dataperpustakaan','w')

while True:
    kode = input('Masukan Kode Member   : ')
    nama = input('Masukan Nama Member   : ')
    buku = input('Masukan Judul Buku    : ')
    ulang = input('ulang lagi(y/n)  : ')
    skrng = datetime.date(datetime.now())
    balik = skrng + timedelta(days=7)
    myfile = open('d:\dataperpustakaan','a')
    myfile.write('{}|{}|{}|{}|{}\n'.format(kode,nama,buku,skrng,balik))
    if ulang == 'y':
        continue
    else:
        break

myfile = open('d:\dataperpustakaan','r')
isi = myfile.read()
print(isi)

myfile.close()

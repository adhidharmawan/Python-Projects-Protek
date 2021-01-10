from datetime import* 

def diffDate(skrng2) :
    global skrng
    skrng = datetime.date(datetime.now())
    skrng2 = datetime.strptime(skrng2, "%Y-%m-%d").date()
    selisih = int((skrng - skrng2).days)
    return selisih

myfile = open('d:\dataperpustakaan','r')
isi2 = myfile.read()
print(isi2)
myfile = open('d:\dataperpustakaan','r')
isi = myfile.readlines()

masuk = input('Masukkan Kode Member  : ')

for data in range(len(isi)):   
    if masuk in isi[data]:
        pisah = isi[data].split('|')
        maks = pisah[4].rstrip('\n')
        batas = diffDate(maks)
        if batas <= 0:      
            telat = '-'
            denda = '-'     
        if batas > 0:   
            telat = str(batas),'hari'
            denda = 'Rp ' + str(batas * 2000)
        print('\nData Peminjaman Buku')
        print('Kode Member              : ', pisah[0])
        print('Nama Member              : ', pisah[1])
        print('Judul Buku               : ', pisah[2])
        print('Tanggal Mulai Peminjaman : ', pisah[3])
        print('Tanggal Maks Peminjaman  : ', maks)
        print('Tanggal Pengembalian     : ', skrng)
        print('Terlambat                : ', telat)
        print('Denda                    : ', denda)

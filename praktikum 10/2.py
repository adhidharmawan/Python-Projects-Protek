myfile = open('d:\dataMahasiswa.txt', 'w')

while True :
    nim = input('Masukkan NIM : ')
    nama = input('Masukkan Nama Mhs : ')
    alamat = input('Masukan Alamat : ')
    ulang = input('Ulangi input lagi (y/n): ')
    myfile = open('d:\dataMahasiswa', 'a')
    myfile.write('{} | {} | {} \n'.format(nim,nama,alamat))

    if ulang == 'y':
        continue
    else:
        break

myfile = open('d:\dataMahasiswa', 'r')
isi = myfile.read()
print(isi)

myfile.close()

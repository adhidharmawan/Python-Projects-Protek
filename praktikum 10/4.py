myfile = open('d:\dataMahasiswa', 'r')
data1 = []
data2 = []
data3 = []
for teks in myfile:
    pisah = teks.split('|')
    data1.append(pisah[0])
    data2.append(pisah[1])
    data3.append(pisah[2])

masuk = str(input('Masukan NIM yang mau dicari: '))

if masuk in data1:
    i = data1.index(masuk)
    print('Data Mahasiswa')
    NIM = data1[i]
    Nama = data2[i]
    Alamat = data3[i]
    print('NIM   : ',NIM,'\nNama  : '+Nama, '\nAlamat: '+Alamat)

if masuk not in data1:
    print('Data mahasiswa tidak ditemukan')

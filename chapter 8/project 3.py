jmlh =int(input('Berapa jumlah mahasiswa yang akan di input: '))

data = []
a = 1
for a in range(jmlh):
    a +=1
    nama = str(input('Masukan nama mahasiswa/i ke-'+str(a)+':'))
    data.append(nama)
data.sort()
i = 0
for i in range(len(data)):
    print(data[i],'(',len(data[i]),'karakter)')
    i +=1

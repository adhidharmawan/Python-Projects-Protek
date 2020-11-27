try :
    namafile = input('Masukkan nama file: ')
    bukafile = open(namafile, 'r')
    bukafile = open(namafile, 'a')
    
    while True:
        isifile = input('Data yang mau ditambahkan : ')
        bukafile.write('\n')
        bukafile.write(isifile)
        lagi = input('Mau lagi? (y/n)')
        if lagi != 'y' :
            break
        elif lagi == 'n' :
            break
    bukafile = open(namafile, 'r')
    print(bukafile.read())
    bukafile.close()
except FileNotFoundError :
    print('File tidak ditemukan')

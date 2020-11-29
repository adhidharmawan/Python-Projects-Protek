print('='*8,'Daftar Menu ','='*8)
print('apel     :Rp. 5000')
print('jeruk    :Rp. 8500')
print('mangga   :Rp. 7800')
print('duku     :Rp. 6500')
print('='*30)
print('Menu:')
print('A. Tambah data buah')
print('B. Beli buah')
print('='*30)

daftar = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
while True:
    pilih = input('Masukakan pilihan (A/B): ')
    if pilih == 'A':
        tambah = str(input('Nama buah yang di tambah: '))
        if tambah in daftar:
            print('Buah sudah ada dalam menu')
        elif tambah not in daftar:
            harga = int(input('Berapa harga buah: '))
            daftar.update({tambah:harga})
            ulang = str(input('Mau tambah lagi(y/n)?:'))
            if ulang == 'y':
                continue
            if ulang != 'y':
                for x, y in daftar.items():
                    print(x,':',y)
                break
            
        continue
    if pilih == 'B':
        total2 = 0
        try:
            while (daftar):
                buah = str(input('Nama buah yang dibeli:'))
                kg = float(input('Berapa Kg : '))
                total2 += kg*daftar[buah]
                ulang = input('Mau beli yang lain(y/n)?:')
                if ulang == 'y':
                    continue
                if ulang != 'y':
                    print('='*30)
                    print('Total harga:', total2)
                    break
            break
        except ValueError:
            print('Nama buah tidak ada')
        except KeyError:
            print('Nama buah tidak ada')


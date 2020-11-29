print('Daftar Menu:')
print('apel     :Rp. 5000')
print('jeruk    :Rp. 8500')
print('mangga   :Rp. 7800')
print('duku     :Rp. 6500')

daftar = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
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
            print('-'*25)
            print('Total harga:', total2)
            break
except ValueError:
    print('Nama buah tidak ada')

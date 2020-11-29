print('Daftar Menu:')
print('apel     :Rp. 5000')
print('jeruk    :Rp. 8500')
print('mangga   :Rp. 7800')
print('duku     :Rp. 6500')

daftar = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
try:
    while (daftar):
        buah = input('Nama buah yang dibeli:')
        kg = float(input('Berapa Kg : '))
        total = kg*daftar[buah]
        print('Total harga:', total)
        break
except ValueError:
    print('Nama buah tidak ada')

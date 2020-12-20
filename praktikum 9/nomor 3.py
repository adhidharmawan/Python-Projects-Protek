def bintang(n):
    for i in range(n):
        baris = (('*'*(1+(i-2)*2)).center(1+2*n))
        print(baris)
        
    for i in range(n):
        baris = (('*'*(n+(i-1)*-2)).center(1+2*n))
        print(baris)

while True:
    bil = int(input('Masukan jumlah bilangan: '))
    if bil %2==1:
        bintang(bil)
        break
    else:
        print('Bilangan harus ganjil')
        ulang = input('Ulang y/n : ')
        if ulang == 'y':
            continue
        else:
            break

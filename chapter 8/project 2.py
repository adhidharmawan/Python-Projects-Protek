def dataStat(x):
    #menghitung rata rata(a)
    bilangan = len(x)
    jumlah = sum(x)
    rata = jumlah/bilangan
    a = rata

    #menentukan nilai tertinggi(b)
    tinggi = max(x)
    b = tinggi
    
    #menentukan nilai terendah(c)
    rendah = min(x)
    c = rendah

    #list data
    dataStat = [a, b, c]
    print(dataStat)

data = (1,2,3,4,5)
print(data)
dataStat(data)

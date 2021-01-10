from datetime import*

def diffDate(x):
    skrng = x.split('-')
    pisah = []
    for data in skrng:
        skrng = x.split('-')
        pisah.append(int(data))
    tanggal1 = datetime.date(datetime.now())
    tanggal2 = date(pisah[0],pisah[1],pisah[2])
    selisih = (tanggal2 - tanggal1).days
    print(selisih)

diffDate('2018-12-30')

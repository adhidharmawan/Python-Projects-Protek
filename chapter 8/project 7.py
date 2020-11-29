def harga(buah):
    data = list(buah.values())
    data.sort(reverse=True)
    draft=data[0]
    for x,y in buah.items():
        if y == draft:
            print(x)

daftar = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
harga(daftar)

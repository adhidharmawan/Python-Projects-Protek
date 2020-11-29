def rata(buah):
    data = tuple(buah.values())
    jmlharga = sum(data)
    jmlbuah = len(data)
    hasil = jmlharga/jmlbuah
    print(hasil)

daftar = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
rata(daftar)

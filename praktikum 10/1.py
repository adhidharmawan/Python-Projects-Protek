def membaca(data):
    myfile = open(data, 'r')
    ganjil = 0
    genap = 0
    for i in myfile:
        if int(i) % 2 == 0 :
            genap += 1
        elif int(i) % 2 == 1 :
            ganjil += 1
    myfile.close()
    hasil = {"genap" : genap, "ganjil" : ganjil}
    return hasil

data = "data.txt"
print("Banyaknya bilangan genap : ", membaca(data).get('genap'))
print("Banyaknya bilangan ganjil: ", membaca(data).get('ganjil'))

#segitiga bintang ajaib

bintang = ""
baris = 5

while (baris >= 0):
    kolom = baris

    while (kolom > 0):
        bintang = bintang + "*"
        kolom = kolom - 1
    bintang = bintang + "\n"
    baris = baris - 1
print(bintang)

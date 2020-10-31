#segitiga bintang ajaib

bintang = ""
baris = 1

while (baris <= 5):
	kolom = baris

	while (kolom > 0):
		bintang = bintang + "*"
		kolom = kolom - 1	
	bintang = bintang + "\n"
	baris = baris + 1
print (bintang)

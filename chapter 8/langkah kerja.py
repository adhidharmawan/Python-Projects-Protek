print('='*38)
#1.membuat list
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print(a)
print(b)
print('='*38)

#2.menyisipkan nilai
a.insert(3, 10)
b.insert(2, 15)
print(a)
print(b)
print('='*38)

#3.menyisipkan nilai
a.append(4)
b.append(8)
print(a)
print(b)
print('='*38)

#4.melakukan sorting
a.sort()
b.sort()
print(a)
print(b)
print('='*38)

#5.membuat list c dan d
c = (a[0:8])
d = (b[2:10])
print(c)
print(d)
print('='*38)

#6.membuat list e
e = []
i = 0
for i in range (len(c)):
    e = e + [c[i] + d[i]]
print(e)
print('='*38)

#7.mengubah list ke tuple
print(tuple(e))
print('='*38)

#8.cari nilai min,maks, dan jumlah elemen dari e
print(max(e))
print(min(e))
print(sum(e))
print('='*50)

#9.buat string
myString = 'python adalah bahasa pemrograman yang menyenangkan'
print(myString)
print('='*50)

#10.mencari penyusun karakter huruf
karakter = set(myString)
print(karakter)
print('='*50)

#11.mengurutkan karakter huruf sesuai alfabet
lis= list(karakter)
lis.sort()
print(lis)
print('='*50)

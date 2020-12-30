file = open('d:/bilangan.txt','a+')
bil1 = []
bil2 = []
i = 0

for data in file:
    pisah = data.split('|')
    bil1.append(pisah[0])
    bil2.append(pisah[1].strip())
    jml = int(bil1[i]) + int(bil2[i])
    file.write(str(jml))
    i +=1
file.close()

jmlh = open('d:/bilangan.txt','r')
print(jmlh.read())
jmlh.close()

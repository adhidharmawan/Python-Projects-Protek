def kuadrat(bil):
    data = []
    for i in range(len(bil)):
        bil[i]**=2
    return bil
    
jml = int(input('Jumlah bilangan yang ingin dimasukkan:'))
bil=[]
for i in range(jml):
    try:
        bilangan = int(input('Masukkan bilangan:'))
        bil.append(bilangan)
    except ValueError:
        print('Data yang anda masukkan salah')
print(kuadrat(bil))

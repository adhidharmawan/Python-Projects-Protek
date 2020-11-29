data = []
jmlbil = int(input('Berapa bilangan yang ingin dimasukkan: '))

a = 1
while True:
    try:
        bilangan = int(input('Masukan bilangan bulat ke-'+ str(a)+ ':'))
        data.append(bilangan)
        a += 1
        if a == jmlbil +1:
            break
    except ValueError:
        print('Input data salah')

data.sort(reverse = True)
print(data)

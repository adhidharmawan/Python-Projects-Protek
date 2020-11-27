print('------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('------------------------')
def ratarata():
    try:
        global bilangan
        bilangan = int(input('Masukan bilangan bulat: '))
    except ValueError :
        print('bukan bilangan bulat')
x = 0
sum = 0
while True:
    ratarata()
    x += 1
    sum += bilangan
    rata = sum/x
    lagi =(input('Lagi (y/n)? : '))
    if lagi == 'n' :
        break
    elif lagi != 'y':
        break
print('Rata-ratanya adalah : ',rata)

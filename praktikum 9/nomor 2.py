def bintang(n):
    for i in range(n):
        baris = (('*'*(1+2*i)).center(1+2*n))
        print(baris)
    
bintang(4)

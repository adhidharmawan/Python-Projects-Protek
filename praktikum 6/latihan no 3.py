def factorial(n):
    facto=1
    while(n>0):
        facto=facto * n
        n = n - 1
    return facto


def kombinasi(p,q):
    kombinasi = factorial(p) / (factorial(q) * factorial(p-q))
    print(kombinasi)

def permutasi(s,t):
    permutasi = factorial(s) / factorial(s-t)
    print(permutasi)

kombinasi(5,3)
permutasi(10,7)

def sum(*n):
    u = 0
    for s in n:
       u = u + s
    return u

def average(*n):
    u = 0
    for s in n:
        u = u + s
        average = sum(*n) / u
    return average

def maks(*n):
    mak = n[0]
    for u in n:
        if u > mak :
            mak = u
    return mak

def min(*n):
    mini = n[0]
    for u in n:
        if u < mini :
            mini = u
    return mini
    

import random
def shuffleString(x,n):
    melist = []
    a = 0
    while True:
        data = [''.join(random.sample(x,len(x)))]
        melist +=data
        a = a + 1
        if a == n:
            break
    print(melist)
        
shuffleString('aku',1)
shuffleString('aku',2)
shuffleString('aku',3)
shuffleString('aku',4)

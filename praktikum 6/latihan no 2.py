q = 4
for b in range(0, q):
    for c in range(0, b + 1):
        print('* ' , end='')
    print('')

r = 4
for b in range(0, r):
    for c in range(0, r - 1):
        print('* ' , end='')
    r -= 1
    print('')

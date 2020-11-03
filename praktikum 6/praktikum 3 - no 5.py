from operation import *

a = 2
b = 4
c = 5
d = 6
e = 7
f = 9
g = 10
h = 12
i = 34

print('a.', a, '+', b, '*', d, '-', b, '=', jumlah(a,kurang(kali(b, d),b)))
print('b. (', b, '+', e, ')*(', d, '-', f, ')=',kali(jumlah(b,e), kurang(d, f)))
print('c. (', g, '+', a, ')/(', e, '+', c, ')/(', h, '-', i, ')=', bagi(bagi(jumlah(g,a),jumlah(e,c)), kurang(h,i)))

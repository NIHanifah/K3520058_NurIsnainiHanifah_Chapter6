from operation import *

a = 10
b = 7
print(a, '+', b, '=', jumlah(a, b))
print(a, '-', b, '=', kurang(a, b))
print(a, 'x', b, '=', kali(a, b))
print(a, '/', b, '=', bagi(a, b))

a = 2
b = 3
c = 5
d = 4
e = 34
print(a, '+', d, '*', jumlah(a, d), '-', d, '=', kali(jumlah(a, d), kurang(jumlah(a, d), d)))
print('(', d, '+', jumlah(c, a), ') * (', jumlah(a, d), '-', jumlah(c, d), ') =', kali(jumlah(d, jumlah(a, c)), kurang(jumlah(a,d), jumlah(c,d))))
print('(', kali(a, c), '+', a, ') / (', jumlah(a, c), '+', c, ') / (', kali(b, d), '-', e, ') =', 
bagi(bagi(jumlah(kali(a, c), a), jumlah(jumlah(a, c), c)), kurang(kali(b, d), e)))
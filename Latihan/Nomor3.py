#Rumus faktorial
def faktorial(n):
    x = 1
    while n >= 1:
        x = x * n
        n = n - 1
    return x
    
print(faktorial(4))

#Kombinasi
C = faktorial(5) / (faktorial(3) * faktorial(2))
print('C(5, 3)= ', C)

#Permutasi
P = faktorial(10) / faktorial(3)
print('P(10, 7)= ' ,P)
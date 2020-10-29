def sum(*myData1):
    sum = 0
    for data in myData1:
        sum += data
    print('Jumlah: ', sum)

sum(1, 2, 3, 4, 5)

#Mencari rata-rata
def avarage(*myData2):
    sum = 0
    i = 1
    for data in myData2:
        sum += data
        i += 1
    rata2 = sum/i
    print('Rata-rata: ', rata2)

avarage(1, 2, 3, 4, 5)

#Mencari nilai maksimal
def maks(*myData3):
    result = max(myData3)
    print('Nilai terbesar = ', result)

maks(4, 6, 3, 10)

#Mencari nilai minumum
def minim(*myData4):
    result = min(myData4)
    print('Nilai terkecil = ', result)

minim(4, 6, 3, 10)
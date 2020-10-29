#Mencari rata-rata
def avarage(*myData1):
    sum = 0
    i = 1
    for data in myData1:
        sum += data
        i += 1
    rata2 = sum/i
    print('Rata-rata: ', rata2)

avarage(5, 10, 4, 9, 30, 16, 2, 11)

#Mencari nilai maksimal
def maks(*myData2):
    result = max(myData2)
    print('Nilai terbesar = ', result)

maks(5, 10, 4, 9, 30, 16, 2, 11)

#Mencari nilai minumum
def minim(*myData3):
    result = min(myData3)
    print('Nilai terkecil = ', result)

minim(5, 10, 4, 9, 30, 16, 2, 11)
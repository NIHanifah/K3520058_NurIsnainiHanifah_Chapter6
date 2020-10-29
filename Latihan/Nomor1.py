def isPythagoras(a, b, c):
    sisi1 = a % 3 
    sisi2 = b % 4
    sisi3 = a % 4
    sisi4 = b % 3
    sisiMiring = c % 5
    if sisi1 == 0 and sisi2 == 0 and sisiMiring == 0 :
        print ("True")
    elif sisi3 == 0 and sisi4 == 0 and sisiMiring == 0 :
        print("True")
    else:
        print ("False")


a = int(input('a = ')) 
b = int(input('b = '))
c = int(input('c = '))
isPythagoras(a, b, c)



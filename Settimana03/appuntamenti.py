# Traduzione in Python dell'esercizio 3 del Lab 01

start1 = int(input("Orario di inizio del  primo  appuntamento: "))
end1   = int(input("Orario di fine   del  primo  appuntamento: "))
start2 = int(input("Orario di inizio del secondo appuntamento: "))
end2   = int(input("Orario di fine   del secondo appuntamento: "))


if start1>start2:
    s = start1
else:
    s = start2

# print("s=",s)

if end1<end2:
    e = end1
else:
    e = end2

# print("e=",e)


if s<e:
    print("Gli appuntamenti si sovrappongono")
else:
    print("Gli appuntamenti non si sovrappongono")




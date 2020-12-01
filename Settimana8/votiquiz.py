voti = [8, 7, 8.5, 9.5, 7, 5, 10, 5]

# fai la somma di tutti e sottrai il minimo
print(sum(voti) - min(voti))
# se il voto minimo è ripetuto, lo toglie una volta sola

# fare sort e togliere il primo elemento
voti2 = list(voti)  # voti[:]
voti2.sort()
voti2.pop(0)
print(sum(voti2))
# se il voto minimo è ripetuto, lo toglie una volta sola

voti2 = list(voti)
minVoti = min(voti2)
voti2.remove(minVoti)
print(sum(voti2))

print(voti)

## SE INVECE VOLESSIMO RIMUOVERE TUTTE LE VOLTE IL MINIMO

# conta quante volte compare il mimimo
minVoti = min(voti)
conta = 0
for x in voti:
    if x == minVoti:
        conta = conta + 1

conta = voti.count(min)
print(sum(voti) - minVoti * conta)

##
# minimo = min(values)
# while minimo in values:
#   values.remove(minimo)
# voto = sum(values)
# print(voto)

# CTRL /  per commentare/scommentare una riga o un blocco di righe

# oppure non potrei costruire un'altra lista con sorted?
voti2 = sorted(voti)
voti2.pop(0)
# oppure voti2 = voti2[1:]
# oppure, contorta: voti2[0:1] = []
print(sum(voti2))

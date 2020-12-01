# leggere un'orario nella format ore:minuti (es: 10:30)

orario = input("Orario (formato hh:mm): ")

# esempio: "10:30", "9:00", "09:00", "1234" NO, "ciao"NO, "10:00:00" NO

# "10:5" non valido
# "10:"

trovatiErrori = False

# controllo se c'è il : e dove si trova
# pos = posizione dove si trova il :
# potrà essere pos==2 oppure pos==1
pos = orario.find(':') #cerco la posizione del :

# valuto dove si trova il :
if pos == 2:
    # : in terza posizione, come 00:00
    # estraggo ore e minuti (ma ancora come stringhe)
    if len(orario) == 5:
        ore = orario[0]+orario[1]
        minuti = orario[3]+orario[4]
    else:
        print("Formato ora non valido")
        trovatiErrori = True
elif pos==1:
    # : in seconda posizione, come 0:00
    if len(orario) == 4 :
        ore = orario[0]
        minuti = orario[2]+orario[3]
    else:
        print("Formato ora non valido")
        trovatiErrori = True
elif pos==-1:
    # non c'è proprio (es, ciao, 1234)
    print("Manca il simbolo : , dato non valido")
    trovatiErrori = True
else:
    # c'è ma è in una posizione diversa (es. :00. 000:00, ...)
    print("Formato ora non valido")
    trovatiErrori = True

# abbiamo controllato il formato x:xx oppure xx:xx e separato le due parti
# prima/dopo il :, salvandole in due STRINGHE diverse

# DA QUI IN AVANTI dobbiamo proseguire SOLO se non ci sono state anomalie
# «« ma ho trovato errori prima??? »»
if not trovatiErrori:
#if trovatiErrori==False:
    print("ho trovato: ", ore, minuti)

    # estrai valore numerico dell'ora
    if ore.isnumeric():
        ore = int(ore)
        if not(0<=ore<=23):
            print("Ore non valide")
            trovatiErrori = True
    else:
        print("Le ore non sono numeriche")
        trovatiErrori = True

    if not trovatiErrori:
        if minuti.isnumeric():
            minuti = int(minuti)
            if not(0<=minuti<=59):
                print("Minuti non validi")
                trovatiErrori = True
        else:
            print("I minuti non sono numerici")
            trovatiErrori = True


# creo una stringa che contiene i caratteri prima del :
# verifico che questa stringa sia lunga 1 o 2 e contenga solo cifre e siano <= 23
# converto la stringa in intero (ore)

# creo una stringa che contiene i caratteri dopo :
# verifici che questa stringa sia lunga 1 o 2 e contenga solo cifre e siano <= 59
# converto la stringa in intero (minuti)


# calcolo un tempo "scalare" in minuti a partire da mezzanotte
start1 = ore * 60 + minuti
print(start1)

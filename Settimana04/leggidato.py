# Lettura di un dato dall'utente controllando che sia nell'intervallo giusto

# ESEMPIO: leggiamo un dato intero tra 1 e 100

valido = False
while not valido:
    dato = int(input("Inserisci un numero tra 1 e 100: "))
    if dato<1 or dato>100: # condizione di errore
        print('Dato errato, ripeti')
    else:
        valido = True


valido = False
while not valido:
    dato = int(input("Inserisci un numero tra 1 e 100: "))
    if 1 <= dato <= 100: # condizione di ok
        valido = True
    else:
        print('Dato errato, ripeti')

while not valido:
    dato = input("Inserisci un numero tra 1 e 100: ")
    if not dato.isnumeric():
        print('Deve essere numerico')
    else:
        dato = int(dato)
        if dato<1 or dato>100: # condizione di errore
            print('Dato errato, ripeti')
        else:
            valido = True

#while valido is True:
#while valido == True:



print(dato)

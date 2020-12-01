from random import randint

## PRIMA VERSIONE: UNO TURNO SOLO DI GIOCO

# 1) computer estrae una carta per sé
carta = randint(1, 10)
print(f"Il banco ha {carta}")
puntiBanco = carta

# 2) computer estrae 2 carte per il giocatore
carta  = randint(1, 10)
print(f'Hai la carta {carta}')
carta2  = randint(1, 10)
print(f'Hai la carta {carta2}')
puntiGiocatore = carta + carta2

# 3) permettiamo al giocatore di giocare
# - stay - hit - sballa
azione = input("Cosa vuoi fare? (c=carta, f=ferma) ")
while azione!='f' and puntiGiocatore<21:
    if azione=='c':
        carta = randint(1, 10)
        print(f'Hai la carta {carta}')
        puntiGiocatore = puntiGiocatore + carta
    else:
        print('Azione non valida')

    if puntiGiocatore<21:
        azione = input("Cosa vuoi fare? (c=carta, f=ferma) ")

#print(puntiGiocatore)

if puntiGiocatore==21:
    print("Complimenti, hai 21! Adesso gioco io")
elif puntiGiocatore>21:
    print("Hai Sballato")
else:
    print(f"Hai {puntiGiocatore} punti. Adesso gioco io")


# 4) il computer gioca SE IL GIOCATORE NON HA SBALLATO
# con una logica che affineremo via via
# - stay - sballa

if puntiGiocatore<=21:
    # devo giocare perché il giocatore non ha sballato
    while puntiBanco<21 and puntiBanco<puntiGiocatore and puntiBanco<17:
         carta = randint(1, 10)
         print(f'Il banco ha preso {carta}')
         puntiBanco = puntiBanco + carta

# 5) si decide chi ha vinto in funzione di:
# chi ha sballato (giocatore, computer, nessuno)
# quanti punti ha ciascuno (se nessuno ha sballato)
if puntiGiocatore>21:
    print("Vince il banco perché il giocatore ha sballato")
elif puntiBanco>21:
    print("Vince il giocatore perché il banco ha sballato")
elif puntiBanco>=puntiGiocatore:
    print(f"Vince il banco con {puntiBanco} punti contro {puntiGiocatore}")
else:
    print(f"Vince il giocatore con {puntiGiocatore} punti contro {puntiBanco}")

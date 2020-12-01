richter = float(input("Richter: "))

if richter >= 8.0:
    print("Cadono tutti")
else:
    if richter >= 7.0:
        print("Cadono molti")
    else:
        if richter >= 6.0:
            print("Molti danneggiati")
        else:
            if richter >= 4.5:
                print("Danni alle catapecchie")
            else:
                print("Nessun danno")


if richter >= 8.0:
    print("Cadono tutti")
elif richter >= 7.0:
    print("Cadono molti")
elif richter >= 6.0:
    print("Molti danneggiati")
elif richter >= 4.5:
    print("Danni alle catapecchie")
else:
    print("Nessun danno")


# ERRORE: vengono eseguiti più rami, non uno solo
if richter >= 8.0:
    print("Cadono tutti")
if richter >= 7.0:
    print("Cadono molti")
if richter >= 6.0:
    print("Molti danneggiati")
if richter >= 4.5:
    print("Danni alle catapecchie")
else:
    print("Nessun danno")





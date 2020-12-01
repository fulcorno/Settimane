from random import uniform

TENTATIVI = 1000000

interno = 0
for i in range(TENTATIVI):
    # genero un punto casuale in [-1,1]x[-1,1]
    x = uniform(-1, 1)
    y = uniform(-1, 1)

    # verifico se il punto è interno al cerchio
    if x*x + y*y <= 1:
        interno = interno + 1

#print(interno, TENTATIVI)

# interno : TENTATIVI = area cerchio : area quadrato
# interno : TENTATIVI = PI * 1^2 : 4
# PI = 4 * interno / tentativi

pi = 4 * interno / TENTATIVI
print (f"Pigreco vale {pi}")


values = [ 3, 7, 11, 110, 95, 115 ]

limit = 100
pos = 0

found = False
while pos < len(values):
    if values[pos] > limit:
        if not found:
            posFound = pos
        found = True

    pos=pos+1

if found:
    print(f'Trovato in posizione {posFound}')
else:
    print('Non trovato')

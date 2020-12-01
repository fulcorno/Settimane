N = 10
K = 4

#print('Questa è la riga di intestazione')
for p in range(1, K+1):
    #print(f'x^{p:<8d}', end='')
    titolo = f'x^{p}'
    print(f'{titolo:>10s}', end='')
print()
print()

for x in range(1, N+1):

    # print(f'Questa è la riga per x={x}')
    for p in range(1, K+1):
        print(f'{x**p:10d}', end='')
    print()


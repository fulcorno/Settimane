count = 0
ok = True

while (count<10) and ok :
    a = int(input("N: "))

    if a==0:
        ok = False
    else:
        print( f'Numero {count+1} = {a}')
    count = count + 1

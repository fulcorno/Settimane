import math

r = float(input("Raggio: "))
area = math.pi * (r**2)

print("L'area del cerchio di raggio", r, "vale", area)

print("L'area del cerchio di raggio "+str(r)+" vale "+str(round(area,2)))

print("L'area del cerchio di raggio %.2f vale %.2f" % ( r, area ) )

print(f"L'area del cerchio di raggio {r:.2f} vale {area:.2f}")

print(f"L'area del cerchio di raggio {r:.2f} vale {math.pi * r**2:.2f}")


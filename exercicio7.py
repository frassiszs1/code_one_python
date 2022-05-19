import math

x_1 = int(input("digite a coordenada x_1: "))
x_2 = int(input("digite a coordenada x_2: "))
y_1 = int(input("digite a coordenada y_1: "))
y_2 = int(input("digite a coordenada y_2: "))

def distancia():
    dist = math.sqrt(((x_2 - x_1)**2) + ((y_2 - y_1)**2))
    return print(f"{dist:,.2f}")
    
distancia()

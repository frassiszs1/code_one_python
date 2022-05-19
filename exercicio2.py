valor_digitado = float(input("digite um valor: "))

if valor_digitado > 0 and valor_digitado <= 25:
    print("[0,25]")

elif valor_digitado > 25 and valor_digitado <= 50:
    print("[25,50]")

elif valor_digitado > 50 and valor_digitado <= 75:
    print("[50,75]")

elif valor_digitado > 75 and valor_digitado <= 100:
    print("[75,100]")

elif valor_digitado < 0:
    print("Fora de intervalo")

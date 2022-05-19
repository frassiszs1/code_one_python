print("Responda com (1) para sim e (0) para nao: ")

mora = int(input("Mora perto da vitima? "))
trabalhou = int(input("Já trabalhou com a vitima? "))
telefonou = int(input("Telefonou para a vitima? "))
esteve = int(input("Esteve no local do crime? "))
devia = int(input("Devia para a vitima? "))

soma = mora + trabalhou + telefonou + esteve + devia
if soma == 5:
    print("assassino")
if soma >= 3 and soma <= 4:
    print("cumplice")
if soma == 2:
    print("suspeito")
if soma < 2:
    print("liberado")

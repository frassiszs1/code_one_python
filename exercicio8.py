import math

i = 1
soma = 0
termos = 1000
    
while(i <= termos):
    soma = soma + (1/(math.factorial(i)))
    i += 1 

print(i)
print(soma)

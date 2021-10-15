import math

N = 400
Res = math.sqrt(N)
print(Res)

# # numero = 2
# # raiz_numero = math.sqrt(numero)

# # exp2 = math.exp(2)
# # print(raiz_numero)

# # x = dir(math)
# # print(raiz_numero, exp2)

# a = 3
# b =  2
# resposta1 = a / b
# resposta2 = a // b  # divisao para baixo
# resposta3 = -a // b
# resposta4 = b ** (1/2)
# print(resposta1, resposta2, resposta3,resposta4)   #  resposta3 é muito estranho 

# Exercicio 
# 1
a = 3
b = 5
c = 2

bhaskara = b ** 2 - 4 * a * c
x1 = (-b - (bhaskara** 0.5)) / (2 * a)
x2 = (-b + (bhaskara** 0.5)) / (2 * a)


x1_0 = math.ceil(x1)
x2_0 = math.ceil(x2)
print('Esses resultados são válidos se o valor do bhaskara é positivo')
print(f'O valor do bhaskara é : {bhaskara}\nAs raízes reais são {x1_0} e {x2_0} com resultado arredondado para baixo')
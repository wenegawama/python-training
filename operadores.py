import math

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
print(f'O valor do bhaskara é : {bhaskara}\nAs raízes reais são {x1} e {x2} e {x1_0} e {x2_0} com resultado arredondado para baixo')


#2

x = 8
raiz_cubica = math.pow(x, 1/3)
print(raiz_cubica)

#
import math
import cmath
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

#3
"O resultado é igual pois esta expressão '2*23+7*50' é um string."      

# 4 

numero = 2
resto = numero % 2
print('O numero é par se o resto é 0 e impar se o resto é 1')
n = float(input('Digite um número: '))
r = n % 2
if r == 0:
    print(f'O numero digitado {n} é par')
else:
    print(f'O numero digitado: {n} é impar')


# 5 Area de um area_do_circulo
raio = 2
area_circulo = cmath.pi * math.pow(raio, 2)
print(f'A area do circulo é : {area_circulo}')

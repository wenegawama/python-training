import math
import cmath
valor_digitado = int(input("Digite o valor a calcular : "))

raiz_quadrada_valor_digitado = math.sqrt(valor_digitado)
if raiz_quadrada_valor_digitado > 10 :
    print(True)
else:
    print(False)
    
raio_circunferencia = raiz_quadrada_valor_digitado

area_circunferencia = cmath.pi * math.pow(raio_circunferencia, 2)
circunferencia = 2 * cmath.pi * raio_circunferencia

print("Area :",area_circunferencia)
print("Circunferencia :",circunferencia)

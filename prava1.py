

velocidade_maxima = int(input('Insera a velocidade maxima permitida: '))
velocidade_observada = int(input('Insera a velocidade observada: '))

limit_excesso1 = velocidade_maxima * 1.1
limit_excesso2 = velocidade_maxima * 1.2
limit_excesso3 = velocidade_maxima * 1.5

excesso = velocidade_observada - velocidade_maxima
print(excesso)
if velocidade_observada < limit_excesso1:
    print('Velocidade permitida')

elif velocidade_observada > limit_excesso1 and  limit_excesso2:
    print('Velocidade excedida em {}%'.format(excesso))
    print('Infração: média')
    print('Pontos na carteira : 4')
    print('Multa recebida : r$150,00')
elif velocidade_observada > limit_excesso2 and  limit_excesso3:
    print('Velocidade excedida em {}%'.format(excesso))
    print('Infração: grave')
    print('Pontos na carteira : 5')
    print('Multa recebida : r$200,00')
elif velocidade_observada > limit_excesso3:
    print('Velocidade excedida em {}%'.format(excesso))
    print('Infração: gravíssima')
    print('Pontos na carteira : 7')
    print('Multa recebida : r$900,00')


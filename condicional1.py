
# carro = 'suziki'
# if (carro.title() != 'SUZIKI') :
#     print('Acertou')
# elif (carro.lower() == 'suziki'):
#     print(' acertou')

# resposta = 7

# if resposta != 42:
#     print('errou,tente novamente')

# idade = int(input('Digite sua idade : '))

# if idade >= 18:
#     print('vc pode dirigir no brasil')
# if idade < 18:
#     print('vc não pode dirigir no brasil')
# if idade >= 16 and idade < 21:
#     print('vc pode dirigir mas não comprar alcool no eua')

# pessoa1= int(input('Digite a idade da pessoa 1 : '))
# pessoa2=int(input('Digite a idade da pessoa 2 : '))
# papel1 = str(input('Digite o papel : '))
# papel2 = str(input('Digite o papel : '))


# if pessoa1 >=18 or pessoa2 >= 18 and papel1 =='responsavel' or papel2 =='responsavel' and not pessoa1 < 12 or pessoa2 <12:
#     print('ambos assistem o filme no cinema')

# pessoa1 = int(input('Digite a idade da pessoa 1: '))
# papel1 = (input('Qual o papel da pessoa1: '))
# pessoa2 = int(input('Digite a idade da pessoa 2: '))
# papel2 = (input('Qual o papel da pessoa2: '))


# if ((pessoa1 >= 18) or (pessoa2 >= 18)) and ((papel1 == 'responsável')) or ((papel2 == 'responsável') and not ((pessoa1 < 12) or (pessoa2 < 12))):
#   print('Ambos assistem o filme no cinema...')


# carro = 'corolla'

# if carro.lower() == 'civic':
    
#     print('Acertou')
# print('Vamos andar de {}'.format(carro))

# carro = 'civic'
# print(carro.lower() == 'civic')
# print(carro.upper() == 'civic')
# print(carro.title() == 'civic')
# print(carro.capitalize()  == 'civic')


# pessoa1 = 10

# pessoa2 = 30

# papel1 = 'menor'

# papel2 = 'responsavel'

# if ((pessoa1 >= 18) or (pessoa2 >= 18)) and  ((papel1 == 'responsável') or (papel2 == 'responsável')) and not ((pessoa1 < 12) or (pessoa2 < 12)):
    
#     print('Ambos assistem o filme no cinema...')

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Pode dirigir no Brasil...")
if idade < 18:
    print("Não pode dirigir no Brasil!")
if idade > 15:

    print("Pode dirigir nos EUA...")
if idade >= 16 and idade < 21:

    print("Pode dirigir, mas não comprar álcool nos EUA")


# from time import sleep
# n1=int(input('Primeiro número : '))
# n2=int(input('Segundo número : '))
# opção=0
# while opção !=5:
#     print('''    [1] somar
#     [2] multiplicar
#     [3] maior
#     [4] novos números
#     [5] sair do programa''')
#     opção=int(input('>>>>> Qual é sua opção? '))
#     if opção ==1:
#         print('A soma de {} e {} é {}'.format(n1,n2,n1+n2))
#     elif opção == 2:
#         print('A multiplicação de {} e {} é {}'.format(n1,n2,n1*n2))
#     elif opção ==3:
#         if n1>n2:
#             print('O maior entre {} e {} é {}'.format(n1,n2,n1))
#         else:
#             print('O maior entre {} e {} é {}'.format(n1,n2,n2))
#     elif opção == 4:
#         print('Adicionne números novamente: ')
#         n3=int(input('Primeiro número : '))
#         n4=int(input('Segundo número : '))
#         if opção == 1:
#             print('A soma entre {} e {} é {}'.format(n3,n4,n3+n4))
#         elif opção == 2:
#             print('A multiplicação entre {} e {} é {}'.format(n3,n4,n3*n4))
#         elif opção == 3:
#             if n3>n4:
#                 print('O maior entre {} e {} é {}'.format(n3,n4,n3))
#             else:
#                 print('O maior entre {} e {} é {}'.format(n3,n4,n4))
#     elif opção ==5:
#         print('Finalizando')
#     else:
#         print('Opção invalida!Tente novamente')
#     print('='*80)
#     sleep(2)
# print('FIM DO PROGRAMA')




operacao = str(input('Que operação deseja realizar (Digite SAIR para finalizar) : '))

primeiro_numero = int(input('Digite primeiro numero : '))
segundo_numero = int(input('Digite segundo numero : '))


soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero


if operacao == '+':
    print('Resultado : {}'.format(soma))
elif operacao == '*':
    print('Resultado : {}'.format(multiplicacao))
elif operacao == '-':
    print('Resultado : {}'.format(subtracao))
elif operacao == '/':
    print('Resultado : {}'.format(divisao))
else:
    print('Operação Inválida !')


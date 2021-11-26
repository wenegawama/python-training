idade = int(input('Idade :'))
sexo = str(input('Sexo (F/M) :'))

if (sexo.upper() == 'F' and idade >= 18):
    print('Pode se alistar, mas não é obligatório')

if (sexo.upper() == 'M' and idade >= 18):
    print('Alistamento obligatório')
    
if (idade < 18 and sexo.upper() in 'FM'):
    print('Alistamento após os 18 anos')
    
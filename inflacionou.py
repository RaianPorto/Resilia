def solicitaValor(alimento):
    valorAntes = float(input('Valor antes? '))
    valorAgora = float(input('Qual o valor agora? '))
    
    if (valorAgora < valorAntes):
        print(f'O {alimento} diminuiu R$ {valorAntes - valorAgora}!')

    elif (valorAgora == valorAntes):
        print(f'Não houve alteração no preço do {alimento}')

    else:
        print(f'O {alimento} aumentou R$ {valorAgora - valorAntes}!')

alimento = input('Qual o alimento deseja verificar? ')

if alimento == 'tomate':
    solicitaValor(alimento)

elif alimento == 'limao':
    solicitaValor(alimento)

elif alimento == 'laranja':
    solicitaValor(alimento)
    
else:
    print(f'{alimento} não está disponível na nossa feira!')
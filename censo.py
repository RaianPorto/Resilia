print('Bem vindo ao censo resilia!')
print('Informe uma idade negativa para encerrar o sistema')

idade = int(input('Informe sua idade: '))
mediaSalario = 0
salarioTotal = 0
qtdDePessoas = 0
maiorIdade = 0
menorIdade = 9999999999
qtdDeMulheres = 0

while idade >= 0:

    sexo = input('Informe seu sexo: F para Feminino | M para Masculino ')
    salario = float(input('Informe seu salário: '))

    qtdDePessoas += 1
    salarioTotal = salarioTotal + salario

    mediaSalario = salarioTotal / qtdDePessoas

    if idade > maiorIdade:
        maiorIdade = idade
    if idade < menorIdade:
        menorIdade = idade

    if sexo == 'F':
        qtdDeMulheres += 1
    
    idade = int(input('Informe sua idade: '))

print('A média salarial do grupo é de ', mediaSalario)

print('Existem ', qtdDeMulheres, 'mulheres no grupo pesquisado.')

print('A maior idade obtida foi de ', maiorIdade, 'anos.')
print('A menor idade obtida foi de ', menorIdade, 'anos.')
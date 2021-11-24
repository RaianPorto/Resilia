# numDeIdent = int(input('Informe o número de identificação: '))

nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))
nota3 = float(input('Informe a nota 3: '))

mediaExerc = float(input('Informe a média dos exercicios: '))

ma = (nota1 + (nota2 * 2) + (nota3 * 3)) / 7

if(ma >= 9):
    print(f'Sua média de aproveitamento foi {ma}. O conceito do aluno é A. Você foi aprovado, parabens!')

elif (ma >= 7.5 and ma < 9):
    print(f'Sua média de aproveitamento foi {ma}. O conceito do aluno é B. Você foi aprovado, parabens!')

elif (ma >= 6 and ma < 7.5):
    print(f'Sua média de aproveitamento foi {ma}. O conceito do aluno é C. Você foi aprovado, parabens!')

elif (ma >= 4 and ma < 6):
    print(f'Sua média de aproveitamento foi {ma}. O conceito do aluno é D. Que pena, você foi reprovado!')

else:
    print(f'Sua média de aproveitamento foi {ma}. O conceito do aluno é E. Que pena, você foi reprovado!')
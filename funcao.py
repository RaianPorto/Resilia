# def soma(*t):

#     soma = x, y
#     x = x + x
#     y = y + y
#     return x, y

# a = 2
# b = 5
# a, b = soma(a, b)
# # print(s)
# print(a)
# print(b)

def previsaoRodagem(qtdLtGaso, kmMedia):
    kmARodar = qtdLtGaso * kmMedia
    return kmARodar


def dirigirOuBeber(age):
    if age >= 18:
        return 'Já pode dirigir!'
    else:
        return 'Não pode nem dirigir nem beber!'

idade = int(input('Qual a sua idade: '))
print(dirigirOuBeber(idade))

qtdLitros = float(input('Qual a quantidade de litros? '))
KmRodados = float(input('Quantos Km o carro faz por litros? '))
print(previsaoRodagem(qtdLitros, KmRodados))
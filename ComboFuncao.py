def CalcFuncao(a, b, c, d):
    resultFuncao = a * c - b * d
    print(resultFuncao)

def SomaNums(a, b, c, d):
    resultSoma = (a + b + c + d) / 4
    print(resultSoma)

a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))
c = int(input("Informe o terceiro número: "))
d = int(input("Informe o quarto número: "))
    
CalcFuncao(a, b, c, d)
SomaNums(a, b, c, d)
salario = float(input('Qual o salario mensal do funcionario? '))
percReajuste = float(input('Qual o percentual de reajuste? '))

novoSalario = salario + (salario * percReajuste/100)

print('O novo salário é: ', novoSalario)





custoDeFabricaDoCarro = float(input('Qual o valor do carro?'))
porcDoDistr = 0.28 * custoDeFabricaDoCarro
impostos = 0.45 * custoDeFabricaDoCarro

custoFinal = custoDeFabricaDoCarro + porcDoDistr

cc = custoDeFabricaDoCarro + porcDoDistr + impostos
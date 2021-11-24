# idade = int(input('Informe a sua idade: '))

# while idade > 18 and idade < 70:
#     print('Você pode dirigir!')
#     idade = int(input('Informe a sua idade: '))

# print('Você não pode dirigir!')


idade = int(input('Informe a sua idade: '))

while idade > 18 or idade < 70:
    print('Você pode dirigir!')
    idade = int(input('Informe a sua idade: '))

print('Você não pode dirigir!')

if idade > 18 or 
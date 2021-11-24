dia = int(input('Em qual dia você nasceu? '))
mes = input('Em qual mês você nasceu? ')

if ((dia >= 21) and (mes == 'marco' or mes == 'março')) or ((dia <= 20) and (mes == 'abril')):
    print('Você é do signo de Áries!')
    
elif ((dia >= 21) and (mes == 'abril')) or ((dia <= 20) and (mes == 'maio')):
    print('Você é do signo de Touro!')

elif ((dia >= 21) and (mes == 'maio')) or ((dia <= 20) and (mes == 'junho')):
    print('Você é do signo de Gêmeos!')

elif ((dia >= 21) and (mes == 'junho')) or ((dia <= 22) and (mes == 'julho')):
    print('Você é do signo de Câncer!')

elif ((dia >= 23) and (mes == 'julho')) or ((dia <= 22) and (mes == 'agosto')):
    print('Você é do signo de Leão!')

elif ((dia >= 23) and (mes == 'agosto')) or ((dia <= 22) and (mes == 'setembro')):
    print('Você é do signo de Virgem!')

elif ((dia >= 23) and (mes == 'setembro')) or ((dia <= 22) and (mes == 'outubro')):
    print('Você é do signo de Libra!')

elif ((dia >= 23) and (mes == 'outubro')) or ((dia <= 21) and (mes == 'novembro')):
    print('Você é do signo de Escorpião!')

elif ((dia >= 22) and (mes == 'novembro')) or ((dia <= 21) and (mes == 'dezembro')):
    print('Você é do signo de Sagitário!')

elif ((dia >= 22) and (mes == 'dezembro')) or ((dia <= 20) and (mes == 'janeiro')):
    print('Você é do signo de Capricórnio!')

elif ((dia >= 21) and (mes == 'janeiro')) or ((dia <= 18) and (mes == 'fevereiro')):
    print('Você é do signo de Aquário!')

else:
    print('Você é do signo de Peixes!')
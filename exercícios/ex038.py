from time import sleep

nota1 = float(input('Insira sua primeira nota: '))
nota2 = float(input('Insira sua segunda nota: '))
media = (nota1 + nota2) / 2
sleep(0.5)
print(f'Tirando {nota1} e {nota2}, a média do aluno seria {media}.')
print('Agora para a análise...')
sleep(0.5)

if media <= 5.0:
    print('Por não bater a média mínima o aluno foi REPROVADO')
elif 7 > media >= 5:
    print(f'Sua média foi de {media}, uma RECUPERAÇÃO terá de ser feita.')
elif 9 < media >= 7:
    print(f'Meus parabéns! Você está com uma média de {media} e foi APROVADO!')
elif media >= 9.0:
    print(f'Com uma média de {media}, a sua nota está ACIMA DA MÉDIA! Você é um excelente aluno, continue assim!')
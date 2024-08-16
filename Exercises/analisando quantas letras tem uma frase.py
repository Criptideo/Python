#analisador de frases
#vezes aparece a letra escolhida
#em que posição a letra aparece pela primeira vezes
#em que posição ela aparece pela última vez

frase = str(input('Digite uma frase aqui: ')).upper().strip()
letra = str(input('Insira uma letra para ser analisada na frase: ')).upper().strip()

print(f'A letra {letra} aparece {frase.count(letra)} vezes na frase.')
print(f'A letra {letra} apareceu pela primeira vez na {frase.find(letra)+1}° posição.')
print(f'Já para a última aparição da letra {letra}, ela se encontra na {frase.rfind(letra)+1}° posição.')
#.rfind foi feito para achar a última colocação de posição de algo
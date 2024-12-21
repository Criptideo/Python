# PROCURANDO UMA STRING DENTRO DA OUTRA

nome = str(input('Qual o seu nome?: ')).strip()
#strip pra cortar os espaços desnecessários do input

print('Seu nome tem Souza? {}'.format('souza' in nome.lower().split()))
#nome.lower para transformar o souza em minúsculo não importa a forma que ele foi escrito, assim, ele pode indentificar de qualquer maneira
#se colocasse como nome.upper funcinaria da mesma forma

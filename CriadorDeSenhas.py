import random

print('GERADOR DE SENHAS')
print('=' * 17)

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890[?.,;:ç$@!%&*_'

numero_senhas = int(input('Numero de senhas: '))
senha_tamanho = int(input('Tamanho da senha: '))

print('SENHAS GERADAS:')
for i in range(numero_senhas):
    senha = ''
    for c in range(senha_tamanho):
        senha += random.choice(caracteres)
    print(senha)

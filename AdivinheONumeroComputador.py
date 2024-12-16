from random import randint


def adivinhaUsu(valor):
    while True:
        numSecreto = randint(1, valor)
        tentativas = 1
        while True:
            print('-' * 40)
            num = int(input(f'\033[36m{tentativas}\033[m. Escolha um número entre 1 e {valor}: '))
            if num > numSecreto:
                print('Tente novamente. O número secreto é menor.')
            elif num < numSecreto:
                print('Tente novamente. O número secreto é maior.')
            else:
                print(f'Parabéns! Você acertou o número secreto é {numSecreto}!.')
                print(f'Número de Tentativas: {tentativas}')
                break
            tentativas += 1
        print('=' * 30)
        continuar = input('Continuar jogando? [S/N]: ').upper()
        if continuar == 'N':
            print('\033[35mObrigado por jogar com a gente! (^u^)/ \033[m')
            break

#adivinha(100)
def adivinhaComp(x):
    menor = 1
    maior = x
    resposta = ''
    while resposta != 'C' and menor != maior:
        numGerado = randint(menor, maior)
        resposta = input(f'O número {numGerado} é mais alto (A), baixo (B), ou é o correto (C)?: ').upper()
        if resposta == 'A':
            maior = numGerado - 1
        elif resposta == 'B':
            menor = numGerado + 1
        else:
            print(f'Isso ai! O computador acertou o número secreto {numGerado}!')
        

adivinhaComp(100)
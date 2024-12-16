from random import choice
from Palavras import palavras


def validando_palavra(palavras):
    palavra = choice(palavras)
    if '-' in palavra:
        palavra = choice(palavras)
    
    return palavra.upper()


def linha(msg):
    print('\033[34m-' * 30)
    print(f'{msg:^30}')
    print('\033[34m-' * 30,'\033[m')


def jogando():
    palavra = validando_palavra(palavras)
    # o comando set vai tirar pra mim as palavras repitidas
    letras_palavra = set(palavra)
    print(palavra)
    letras_usadas = []
    letras_certas = set()
    tentativa = 6 
    linha('JOGO DA FORCA')
    while True:
        print('\033[36m=' * 30) 
        print(f'\033[mTentativas restantes: \033[35m{tentativa}\033[m')

        # quero mostrar as letras usadas, o join vai mostrar a lista como uma string
        print('Letras usadas: ', ' '.join(letras_usadas))

        # adicionando cada letra no lugar
        print('Palavra atual: ', end='')
        for letra in palavra:
            if letra in letras_usadas:
                print(letra, end=' ')
                letras_certas.add(letra)
            else:
                print('_', end=' ')

        # terminar o jogo 
        print()
        if tentativa == 0:
            linha(f'\033[31mFim de jogo!\nSuas tentativas acabaram.\n\033[36mA palavra era:\033[34m {palavra}\033[m')
            break
        elif len(letras_certas) == len(letras_palavra):
            linha(f'\033[32mParabéns! Você acertou.\n\033[36mA palavra era:\033[34m {palavra}\033[m')
            break

        chute = input('\nAdivinhe uma letra: ').upper().strip()
        if len(chute) > 1:              # se for digitado mais de uma letra
            print('\033[31mPor favor, digite apenas uma letra!\033[m')
        elif chute in letras_usadas: 
            print('\033[30mVocê já tentou essa letra, tente outra.\033[m')
            letras_usadas.remove(chute) # mostra somente uma letra, sem contar a repetição
        else:                           # a tentativa vai diminuir se a letra não estiver na palavra
            if chute not in palavra:
                print(f'\033[30mA letra {chute} não está na palavra.\033[m')
                tentativa -= 1
        letras_usadas.append(chute)
    
    
jogando()
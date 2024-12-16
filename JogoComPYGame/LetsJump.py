import pygame
from sys import exit
from random import randint, choice
from time import sleep

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_andando_1 = pygame.image.load("JogoComPYGame/Gráfico/player/player_walk_1.png").convert_alpha()
        player_andando_2 = pygame.image.load("JogoComPYGame/Gráfico/player/player_walk_2.png").convert_alpha()
        self.player_andando = [player_andando_1,player_andando_2] # Esse precisa do self para acessarmos fora do metodo init
        self.player_index = 0
        self.player_pulando = pygame.image.load("JogoComPYGame/Gráfico/player/jump.png").convert_alpha()

        self.image = self.player_andando[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound("JogoComPYGame/Música/audio_jump.mp3")
        self.jump_sound.set_volume(0.2)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def gravidade(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300: 
            self.rect.bottom = 300

    def animando(self):
        if self.rect.bottom < 300:
            self.image = self.player_pulando
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_andando):self.player_index = 0
            self.image = self.player_andando[int(self.player_index)]
    
    def update(self):
        self.player_input()
        self.gravidade()
        self.animando()

class Obstaculos(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type == 'fly':
            fly_1 = pygame.image.load("JogoComPYGame/Gráfico/fly/fly1.png").convert_alpha()
            fly_2 = pygame.image.load("JogoComPYGame/Gráfico/fly/fly2.png").convert_alpha()
            self.frames = [fly_1,fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load("JogoComPYGame/Gráfico/snail/snail1.png").convert_alpha()
            snail_2 = pygame.image.load("JogoComPYGame/Gráfico/snail/snail2.png").convert_alpha()
            self.frames = [snail_1,snail_2]    
            y_pos = 300
        
        self.animacao_index = 0
        self.image = self.frames[self.animacao_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

    def animando(self):
        self.animacao_index += 0.1
        if self.animacao_index >= len(self.frames): self.animacao_index = 0
        self.image = self.frames[int(self.animacao_index)]

    def update(self):
        self.animando()
        self.rect.x -= 6
        self.destruir()

    def destruir(self):
        if self.rect.x <= -100:
            self.kill()

# Pontuação
def display_score():
    tempo = int(pygame.time.get_ticks()/1000) - tempo_inicial
    sup_score = fonte.render(f"Pontos: {tempo}",False,(141, 112, 145)) # Texto, Anti-Aliasing(AA), cor
    retangulo_score = sup_score.get_rect(center = (400,50))
    tela.blit(sup_score, retangulo_score)
    return tempo

# Colisão
def colidindo():
    if pygame.sprite.spritecollide(player.sprite,obstaculo_grupo,False):
        obstaculo_grupo.empty()
        return False
    else: return True 

def creditos_finais():
    tela.fill((69, 112, 153))
    player_pulando = pygame.image.load("JogoComPYGame/Gráfico/player/jump.png").convert_alpha()
    player_pulando = pygame.transform.rotozoom(player_pulando,0,1.5)
    ret_player_pulando = player_pulando.get_rect(midbottom = (110,330))
    
    sup_ceu = pygame.image.load("JogoComPYGame/Gráfico/Sky.png").convert()
    sup_ceu = pygame.transform.rotozoom(sup_ceu,0,1.5)
    tela.blit(sup_ceu,(0,0))
    tela.blit(player_pulando, ret_player_pulando)

    fonte_creditos = pygame.font.Font("JogoComPYGame/Fonte/MonsterFriendFore.otf", 30)
    titulo = fonte_creditos.render("Obrigado por Jogar!",False,(27, 79, 125))
    ret_titulo = titulo.get_rect(center = (400,40))
    voltar = fonte.render("[ESC] para voltar ao menu",False,(222, 180, 51))
    ret_voltar = voltar.get_rect(center = (400,350))
    tela.blit(titulo, ret_titulo)
    tela.blit(voltar, ret_voltar)

    txt = [
        "Canal usado no desenvolvimento: Clear Code",
        "Desenvolvedora: Letícia Pignatari",
        "Modificações aplicadas: ",
        "Créditos adicionados"
    ]

    for i, pos in enumerate(txt):
        y_pos = 120
        texto = fonte.render(pos,False,(85, 109, 173))
        ret_texto = texto.get_rect(center = (400,y_pos + i * 40))
        tela.blit(texto, ret_texto)

pygame.init()  
tela = pygame.display.set_mode((800,400))  # largura e altura
pygame.display.set_caption("Lets Jump")      # Título da janela
relogio = pygame.time.Clock()
fonte = pygame.font.Font("JogoComPYGame/Fonte/alterebro-pixel-font.ttf", 50) # Tipo da fonte / tamanho da fonte
fonte_titulo = pygame.font.Font("JogoComPYGame/Fonte/MonsterFriendFore.otf", 50)
jogo_ativo = False
creditos = False
tempo_inicial = 0
score = 0

bg_music = pygame.mixer.Sound("JogoComPYGame/Música/music.wav")
bg_music.set_volume(0.1)
bg_music.play(loops = -1)

# Grupos
player = pygame.sprite.GroupSingle()
player.add(Player())

obstaculo_grupo = pygame.sprite.Group()

# Cenário
sup_ceu = pygame.image.load("JogoComPYGame/Gráfico/Sky.png").convert() # Importando um imagem
sup_chao = pygame.image.load("JogoComPYGame/Gráfico/ground.png").convert()

# Tela de introdução
nome_jogo = fonte_titulo.render("Let's Jump",False,(86, 49, 92))
ret_inicio = nome_jogo.get_rect(center = (400,80))

player_parado = pygame.image.load("JogoComPYGame/Gráfico/player/player_stand.png").convert_alpha()
player_parado = pygame.transform.rotozoom(player_parado,0,1.5)
ret_player_parado = player_parado.get_rect(center = (400,200))

texto_jogar = fonte.render("Aperte [ESPAÇO] para iniciar",False,(222, 180, 51))
ret_jogar = texto_jogar.get_rect(center = (400,320))

texto_creditos = fonte.render("Créditos",False,(86, 49, 92))
ret_creditos = texto_creditos.get_rect(center = (80,360))

# Timer
obstaculo_timer = pygame.USEREVENT + 1 # Criando um evento próprio, o +1 é usado para evitar conflito de IDs fixos que o pygame tem  
pygame.time.set_timer(obstaculo_timer,1500) # Programando o evento: evento para ser acionado e o tempo de acionar novamente (ms)

while True:
    for evento in pygame.event.get():   # Captura eventos: interações, como pressionar uma tecla ou fechar janela
        if evento.type == pygame.QUIT:  # Verifica se o usuário tenta fechar a janela
            pygame.quit()               # Desliga todos os módulos do pygame
            exit()                      # Finaliza o programa, saindo do loop principal
        
        # Obstáculo timer
        if jogo_ativo:
            if evento.type == obstaculo_timer:
                obstaculo_grupo.add(Obstaculos(choice(["fly","fly","snail","snail"])))
        else:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                if creditos: # Evita de entrar no jogo direto dos créditos, tendo que voltar ao menu
                    jogo_ativo = False
                else:
                    jogo_ativo = True
                    tempo_inicial = int(pygame.time.get_ticks()/1000)     
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if ret_creditos.collidepoint(evento.pos):
                    creditos = True
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                creditos = False

    if jogo_ativo:
        # Cenário
        tela.blit(sup_ceu, (0,0)) # superfície e posição (x,y) 
        tela.blit(sup_chao, (0,300))
        # Score
        score = display_score()
        recorde = display_score()

        # Player
        player.draw(tela) # Desenhando os sprites
        player.update() # Atualizando todos os sprites

        obstaculo_grupo.draw(tela)
        obstaculo_grupo.update()

        # Colisão 
        jogo_ativo = colidindo()
    else:
        # Tela inicial
        tela.fill((141, 112, 145))
        tela.blit(nome_jogo, ret_inicio)
        tela.blit(player_parado, ret_player_parado)
        
        score_mensagem = fonte.render(f"Pontos: {score}", False, (86, 49, 92))
        score_mensagem_ret = score_mensagem.get_rect(center = (400,330))

        # Mostrar score assim que morrer
        if score == 0: tela.blit(texto_jogar, ret_jogar)
        else: tela.blit(score_mensagem, score_mensagem_ret)

        tela.blit(texto_creditos, ret_creditos)
        if creditos:
            creditos_finais()
    
    pygame.display.update() # chegando aqui ele vai atualizar no nosso display tudo que criamos
    relogio.tick(60)        # O loop não deve rodar mais rápido que 60x p/seg (fps)
import pygame
from random import randint

pygame.init()

# Configurações iniciais
x, y = 350, 100  # Posição inicial da moto
pos_x, pos_y = 226, 1200  # Posição inicial da polícia
pos_y_a = 800  # Posição inicial da ambulância
pos_y_t = 2000  # Posição inicial do táxi
velocidade = 10
velocidade_outros = 12
timer = 0
tempo_segundo = 0

# Carregando imagens
fundo = pygame.image.load('fundoJogoPythonMini.png')
moto = pygame.image.load('motoCustomMini.png')
policia = pygame.image.load('policia.png')
ambulancia = pygame.image.load('ambulancia.png')
taxi = pygame.image.load('taxi.png')
fox = pygame.image.load('FoxBGMini.png')

# Fonte para o timer
font = pygame.font.SysFont('arial black', 30)
texto = font.render("Tempo: ", True, (255,255,255), (77,147,8))
pos_texto = texto.get_rect()
pos_texto.center = (65, 50)

# Configuração da janela
janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo com Python")

# Loop principal
janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    # Eventos de saída
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    # Movimento da moto
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RIGHT] and (x <= 458):
        x += velocidade
    if comandos[pygame.K_LEFT] and (x >= 269):
        x -= velocidade

    # Criação de retângulos de colisão
    moto_rect = moto.get_rect(topleft=(x, y))
    policia_rect = policia.get_rect(topleft=(pos_x, pos_y))
    ambulancia_rect = ambulancia.get_rect(topleft=(pos_x + 223, pos_y_a))
    taxi_rect = taxi.get_rect(topleft=(pos_x + 126, pos_y_t))

    # Verificação de colisão
    if moto_rect.colliderect(policia_rect) or moto_rect.colliderect(ambulancia_rect) or moto_rect.colliderect(taxi_rect):
        # Exibe a mensagem de colisão e encerra o jogo
        pygame.display.set_caption("Colisão Detectada! Fim de Jogo")
        print("Colisão Detectada! Fim de Jogo")  # Mensagem no console
        pygame.time.delay(2000)  # Aguarda 2 segundos antes de fechar
        janela_aberta = False
        break  # Sai do loop principal

    # Reseta a posição dos veículos quando saem da tela
    if pos_y_a <= -80:
        pos_y_a = randint(800, 1000)
    if pos_y <= -80:
        pos_y = randint(1400, 3000)
    if pos_y_t <= -80:
        pos_y_t = randint(2400, 4000)

    # Timer para o tempo de jogo
    if timer < 20:
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Tempo: "+str(tempo_segundo), True, (255,255,255), (77,147,8))
        timer = 0

    # Movimento dos carros
    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros + 2
    pos_y_t -= velocidade_outros + 10

    # Desenho na tela
    janela.blit(fundo, (0,0))
    janela.blit(moto, (x, y))
    janela.blit(policia, (pos_x, pos_y))
    janela.blit(ambulancia, (pos_x + 223, pos_y_a))
    janela.blit(taxi, (pos_x + 126, pos_y_t))
    janela.blit(texto, pos_texto)
    janela.blit(fox, (0,500))
    pygame.display.update()

pygame.quit()

import pygame
from random import randint
import time

pygame.init()

# Posição inicial da moto e dos carros
x = 350
y = 100
pos_x = 226
pos_y_t = 800  # Taxi
pos_y = 800    # Polícia
pos_y_a = 800   # Ambulância
timer = 0
tempo_segundo = 0
velocidade = 10
velocidade_outros = 20  # Aumentando a velocidade dos outros carros para maior desafio

# Imagens de fundo e dos veículos
fundo = pygame.image.load('fundoJogoPythonMini.png')
moto = pygame.image.load('motoCustomMini.png')
policia = pygame.image.load('policia.png')
taxi = pygame.image.load('taxi.png')
ambulancia = pygame.image.load('ambulancia.png')
fox = pygame.image.load('FoxBGMini.png')
fox_bad = pygame.image.load('FoxBGMiniBad.png')  

# Fonte para o temporizador e mensagem de colisão
font = pygame.font.SysFont('arial black', 30)
texto = font.render("Tempo: ", True, (255, 255, 255), (77, 147, 8))
pos_texto = texto.get_rect()
pos_texto.center = (65, 50)

# Janela do jogo
janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo com Python")

# Variável de controle para manter o jogo aberto
janela_aberta = True
colisao = False  # Variável para detectar colisão

while janela_aberta:
    pygame.time.delay(50)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    # Comandos de movimento
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RIGHT] and x <= 458:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 269:
        x -= velocidade

    # Detecção de colisão
    if (x < pos_x + 111 and x + 91 > pos_x and y < pos_y + 212 and y + 161 > pos_y) or \
       (x < pos_x + 126 and x + 91 > pos_x and y < pos_y_t + 204 and y + 161 > pos_y_t) or \
       (x < pos_x + 223 and x + 91 > pos_x and y < pos_y_a + 221 and y + 161 > pos_y_a):
        colisao = True
        break  # Sai do loop principal após a colisão

    # Movimentação dos carros
    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros + 2
    pos_y_t -= velocidade_outros + 4

    # Reset dos carros ao sair da tela
    if pos_y_a <= -80:
        pos_y_a = randint(800, 1000)
    if pos_y <= -80:
        pos_y = randint(1400, 3000)
    if pos_y_t <= -80:
        pos_y_t = randint(2400, 4000)

    # Temporizador
    if timer < 20:
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Tempo: " + str(tempo_segundo), True, (255, 255, 255), (77, 147, 8))
        timer = 0

    # Atualização da tela
    janela.blit(fundo, (0, 0))
    janela.blit(moto, (x, y))
    janela.blit(policia, (pos_x, pos_y))
    janela.blit(ambulancia, (pos_x + 223, pos_y_a))
    janela.blit(taxi, (pos_x + 126, pos_y_t))
    janela.blit(texto, pos_texto)

    # Exibe a imagem do Fox (normal)
    janela.blit(fox, (0, 500))
    pygame.display.update()

# Loop de animação pós-colisão
if colisao:
    start_time = time.time()
    text_size = 30  # Tamanho inicial do texto de colisão

    while janela_aberta:  # Loop contínuo para a animação até o usuário fechar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
                pygame.quit()
                exit()  # Encerra o programa completamente

        janela.blit(fundo, (0, 0))
        janela.blit(fox_bad, (0, 500))  # Exibe a imagem de colisão do Fox
        
        # Aumenta o tamanho do texto gradualmente
        text_size += 1  # Incremento menor para uma animação mais sutil
        if text_size > 40:
            text_size = 30  # Reinicia o tamanho para criar um efeito pulsante

        colisao_font = pygame.font.SysFont('arial black', text_size)
        colisao_texto = colisao_font.render("COLISÃO!", True, (255, 0, 0))
        colisao_texto_rect = colisao_texto.get_rect(center=(400, 300))

        # Desenha um balão de "crash" ao redor do texto
        pygame.draw.polygon(janela, (255, 215, 0), [
            (colisao_texto_rect.left - 20, colisao_texto_rect.top - 10),
            (colisao_texto_rect.right + 20, colisao_texto_rect.top - 10),
            (colisao_texto_rect.right + 40, colisao_texto_rect.bottom + 10),
            (colisao_texto_rect.left - 40, colisao_texto_rect.bottom + 10),
        ])

        # Desenha o texto "COLISÃO!" centralizado no balão
        janela.blit(colisao_texto, colisao_texto_rect)
        pygame.display.update()
        pygame.time.delay(100)

pygame.quit()
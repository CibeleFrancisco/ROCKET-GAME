import pygame
from random import randint
pygame.mixer.init()
pygame.mixer.music.load("on000003.mp3")
pygame.mixer.music.play()
x= 410#265 555
y= 130
posx=260
posy=800
posya=800
posyb=800
velocidade=20

velocidade_foguetes= 15
fundo= pygame.image.load("fundo.PNG")
foguete= pygame.image.load("fog.PNG")
foguete2= pygame.image.load("fog2.PNG") #vermelho
foguete3= pygame.image.load("fog3.PNG") #azul
foguete4= pygame.image.load("fog4.PNG") #amarelo

janela = pygame.display.set_mode((888,500))
pygame.display.set_caption("JOGO DO TEMPO EM CRIACAO")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            janela_aberta= False
    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_RIGHT] and x<=555:
        x += velocidade
    if comandos[pygame.K_LEFT] and x>=265:
        x -= velocidade

    if posy<=-180 and posya <=-180 and posyb <=-180:
        posy= randint(800,2000)
        posya=randint(800,2000)
        posyb=randint(800,2000)

    posy -=velocidade_foguetes+8
    posya -=velocidade_foguetes +10
    posyb -=velocidade_foguetes +5

    janela.blit(fundo, (0,0))
    janela.blit(foguete, (x,y))
    janela.blit(foguete2,(posx, posy))
    janela.blit(foguete3,(posx+300, posya))
    janela.blit(foguete4,(posx+150, posyb))

    pygame.display.update()
pygame.quit()
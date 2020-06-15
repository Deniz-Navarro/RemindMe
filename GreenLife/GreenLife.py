import pygame,sys
from random import randint
from pygame.locals import *
from juego import *
from worlds import *
global music,sonido,idioma
music = True
sonido = True
idioma=True
def menu():
    pygame.init()
    ventana=pygame.display.set_mode([1280,720])
    salir=False
    fuente1 = pygame.font.SysFont ("Arial",30,True,False)
    black = (0,0,0)
    reloj1=pygame.time.Clock()
    mundo1 = pygame.image.load("assets/Items/mundo1.png").convert_alpha()
    ifondo = pygame.image.load("assets/Fondos/Menu.png").convert_alpha()
    start1 = pygame.image.load("assets/Items/botons1.png").convert_alpha()
    start2 = pygame.image.load("assets/Items/botons2.png").convert_alpha()
    equis1 = pygame.image.load("assets/Items/equis.png").convert_alpha()
    equis2 = pygame.image.load("assets/Items/equis1.png").convert_alpha()
    icon = pygame.image.load("assets/Items/configuracion.png").convert_alpha()
    icon1 = pygame.image.load("assets/Items/configuracion1.png").convert_alpha()
    menu = pygame.mixer.music.load("assets/Sounds/menu.mp3")
    menu = pygame.mixer.music.play(3)
    start = Button(start1,start2,1280/2-100,720/2-225)
    config = Button(icon,icon1,600,425)
    equis = Button(equis1,equis2,600,575)
    cursor1 = Cursor()
    while salir!=True: #Loop principal
        for event in pygame.event.get(): #Corre todos los eventos en pygame
            if event.type == pygame.QUIT:
                salir=True
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(start.rect):
                    munditos(music,sonido,idioma)
                if cursor1.colliderect(config.rect):
                    mopciones()
                if cursor1.colliderect(equis.rect):
                    salir=True
                    pygame.quit()
                    sys.exit()
        cursor1.update()
        ventana.fill(black)
        ventana.blit(ifondo,(0,0))
        start.update(ventana,cursor1)
        equis.update(ventana,cursor1)
        config.update(ventana,cursor1)
        pygame.display.update()

def mopciones():
    pygame.init()
    ventana=pygame.display.set_mode([1280,720])
    salir=False
    fuente1 = pygame.font.SysFont ("Arial",30,True,False)
    fuente2 = pygame.font.SysFont ("Arial",60,True,False)
    blanco = (179,19,176)
    reloj1=pygame.time.Clock()
    ifondo = pygame.image.load("assets/Fondos/opciones.png").convert_alpha()
    isound = pygame.image.load("assets/Items/sonidoh.png").convert_alpha()
    isound2 = pygame.image.load("assets/Items/sonidoh1.png").convert_alpha()
    isoundd = pygame.image.load("assets/Items/soundd.png").convert_alpha()
    isoundd2 = pygame.image.load("assets/Items/sonidod1.png").convert_alpha()
    iespanol = pygame.image.load("assets/Items/espanol.png").convert_alpha()
    ispanish = pygame.image.load("assets/Items/spanish.png").convert_alpha()
    iingles = pygame.image.load("assets/Items/ingles.png").convert_alpha()
    ienglish = pygame.image.load("assets/Items/english.png").convert_alpha()
    back1 = pygame.image.load("assets/Items/back.png").convert_alpha()
    back2 = pygame.image.load("assets/Items/back1.png").convert_alpha()
    cursor1 = Cursor()
    global music
    global sonido
    global idioma
    sonidoh = Button(isound2,isound,450,720/2-180)
    sonidod = Button(isoundd,isoundd2,700,720/2-180)
    ssonidoh = Button(isound2,isound,450,720/20-30)
    ssonidod = Button(isoundd,isoundd2,700,720/2-30)
    espanol = Button(iespanol,iespanol,420,480)
    ingles = Button(iingles,iingles,670,480)
    back = Button(back1,back2,1050,500)
    while salir!=True: #Loop principal
        for event in pygame.event.get(): #Corre todos los eventos en pygame
            if event.type == pygame.QUIT:
                salir=True
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cursor1.colliderect(sonidoh.rect):
                menu = pygame.mixer.music.play(3)
                music = True
            if cursor1.colliderect(sonidod.rect):
                menu = pygame.mixer.music.stop()
                music = False
            if cursor1.colliderect(ssonidoh.rect):
                sonido = True
            if cursor1.colliderect(ssonidod.rect):
                sonido = False
            if cursor1.colliderect(back.rect):
                salir=True
            if cursor1.colliderect(espanol.rect):
                idioma = True
            if cursor1.colliderect(ingles.rect):
                idioma=False
        if music == False:
            sonidoh = Button(isound,isound2,450,720/2-180)
        if music == False:
            sonidod = Button(isoundd2,isoundd,700,720/2-180)
        if sonido == False:
            ssonidoh = Button(isound,isound2,450,720/2-30)
        if sonido == False:
            ssonidod = Button(isoundd2,isoundd,700,720/2-30)
        if music == True:
            sonidoh = Button(isound2,isound,450,720/2-180)
        if music == True:
            sonidod = Button(isoundd,isoundd2,700,720/2-180)
        if sonido == True:
            ssonidoh = Button(isound2,isound,450,720/2-30)
        if sonido == True:
            ssonidod = Button(isoundd,isoundd2,700,720/2-30)
        if idioma == True:
            espanol = Button(iespanol,iespanol,420,480)
            ingles = Button(iingles,iingles,670,480)
            ifondo = pygame.image.load("assets/Fondos/opciones.png").convert_alpha()
        if idioma == False:
            espanol = Button(ispanish,ispanish,420,480)
            ingles = Button(ienglish,ienglish,670,480)
            ifondo = pygame.image.load("assets/Fondos/options.png").convert_alpha()

        cursor1.update()
        ventana.blit(ifondo,(0,0))
        sonidoh.update(ventana,cursor1)
        sonidod.update(ventana,cursor1)
        ssonidoh.update(ventana,cursor1)
        ssonidod.update(ventana,cursor1)
        espanol.update(ventana,cursor1)
        ingles.update(ventana,cursor1)
        back.update(ventana,cursor1)
        pygame.display.update()

menu()

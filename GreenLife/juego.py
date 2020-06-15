import pygame,sys
from random import randint
from pygame.locals import *
import time
import threading
global seconds
seconds = 0
class Character(pygame.sprite.Sprite):
    def __init__(self,lifes,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.ipersonaje = imagen
        self.rect= self.ipersonaje.get_rect()
        self.rect.top = 720/2
        self.rect.left = 1280/2
        self.lifes = lifes
        self.points = 0
        self.salto = False
        self.movei = False
        self.mover = False
        segundos = "0"

    def draw(self,surface,imagen): #Draw Character
        surface.blit(imagen,self.rect)

    def move(self,event,termino,sound1,sonido): #Player move
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.rect.top == 360:
                        self.salto = True
                        if sonido == True:
                            sound1.play()
                if event.key == pygame.K_LEFT:
                    if self.rect.left >0:
                        self.movei = True
                if event.key == pygame.K_RIGHT:
                    if self.rect.left <1280:
                        self.mover = True
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.salto = False
                if event.key == pygame.K_LEFT:
                    self.movei = False
                if event.key == pygame.K_RIGHT:
                    self.mover = False


    def drawl(self,surface,fuente,idioma): #Draw Lifes
        lifess = str(self.lifes)
        if idioma == True:
            clifes=fuente.render("Vidas: "+lifess,0,(0,0,0))
        if idioma == False:
            clifes=fuente.render("Lifes: "+lifess,0,(0,0,0))
        surface.blit(clifes,(100,650))

    def drawp(self,surface,fuente,idioma): #Draw Points
        pointss = str(self.points)
        if idioma==True:
            cpoints=fuente.render("Puntos: "+pointss,0,(0,0,0))
        if idioma==False:
            cpoints=fuente.render("Points: "+pointss,0,(0,0,0))
        surface.blit(cpoints,(1280/2,650))

    def win(self,surface,fuente,idioma): #Draw Win
        if idioma == True:
            lectura=fuente.render("Ganaste",0,(0,0,0))
        if idioma == False:
            lectura=fuente.render("You Win",0,(0,0,0))
        surface.blit(lectura,(1280/2-200,720/2-200))

    def lose(self,surface,fuente,idioma): #Draw Lose
        if idioma == True:
            lectura=fuente.render("Perdiste",0,(0,0,0))
        if idioma == False:
            lectura=fuente.render("You Lose",0,(0,0,0))
        surface.blit(lectura,(1280/2-200,720/2-200))

class Enemy(pygame.sprite.Sprite):
    def __init__(self,speed):
        pygame.sprite.Sprite.__init__(self)
        self.iciclista = pygame.image.load("assets/Items/piedra.png").convert_alpha()
        self.rect= self.iciclista.get_rect()
        self.rect.top = 425
        self.rect.left = 1450
        self.speed = speed


    def draw(self,surface): #Enemy Draw
        surface.blit(self.iciclista,self.rect)

    def collision(self,player,sound2,sonido): #Enemy Collision
        (xr,yr)=(player.rect.left,player.rect.top)
        self.rect.left -= self.speed
        if self.rect.colliderect(player.rect):
            (player.rect.left,player.rect.top)=(xr,yr)
            self.rect.left= 1450
            self.rect.top = 425
            global seconds
            seconds -= 5
            if sonido == True:
                sound2.play()
        if self.rect.left <= -20:
            self.rect.left= 1450
            self.rect.top = 425

class Object(pygame.sprite.Sprite):
    def __init__(self,speed,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.iobject = imagen
        self.rect= self.iobject.get_rect()
        self.rect.top = randint(160,400)
        self.rect.left = randint(1280,1500)
        self.speed = speed


    def draw(self,surface): #Enemy Draw
        surface.blit(self.iobject,self.rect)

    def collision(self,player,points,sound3,sonido): #Enemy Collision
        (xr,yr)=(player.rect.left,player.rect.top)
        self.rect.left -= self.speed
        if self.rect.colliderect(player.rect):
            (player.rect.left,player.rect.top)=(xr,yr)
            self.rect.top = randint(200,400)
            self.rect.left = randint(1280,2000)
            player.points+=points
            if sonido == True:
                sound3.play()
        if self.rect.left <= -40:
            self.rect.top = randint(200,400)
            self.rect.left = randint(1280,2000)
            player.lifes -= 1

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

class Button(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x,y):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
    def update(self,surface,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal

        surface.blit(self.imagen_actual,self.rect)

def Game(endgame,fondo,life,venemy,vobject1,vobject2,goal,pointsg,tlimit,goal2,music,sonido,idioma):
    ss = tlimit
    global seconds
    seconds = tlimit
    def crono():
        if endgame == False:
            global seconds
            seconds -=1
            time.sleep(1)
            return crono()
    pygame.init() #Initialize pygame modules
    ventana=pygame.display.set_mode([1280,720])
    pygame.display.set_caption("GREEN LIFE")
    #Variables
    termino = False
    win=False
    reloj1=pygame.time.Clock()
    fuente1 = pygame.font.SysFont ("Arial",30,True,False)
    fuente2 = pygame.font.SysFont ("Arial",100,True,False)
    texto1= goal
    texto2=goal2
    rojo=(200,20,50)
    verde=(50,205,50)
    blanco=(255,255,255)
    altlimit = False
    cx = 1300
    controlt = 0
    vx=0
    #Music and Sounds
    juego = pygame.mixer.music.load("assets/Sounds/juego.mpeg")
    if music == True:
        juego = pygame.mixer.music.play()
    sound1 = pygame.mixer.Sound("assets/Sounds/salto.wav")
    sound2 = pygame.mixer.Sound("assets/Sounds/damage.wav")
    sound3 = pygame.mixer.Sound("assets/Sounds/point.wav")
    sound4 = pygame.mixer.Sound("assets/Sounds/lose.wav")
    sound5 = pygame.mixer.Sound("assets/Sounds/winner.wav")
    #Images
    if fondo == 1:
        ifondo = pygame.image.load("assets/Fondos/esc11.png").convert_alpha()
        fondoInicial = pygame.image.load("assets/Fondos/esc11.png").convert_alpha()

    if fondo == 2:
        ifondo = pygame.image.load("assets/Fondos/esc2.png").convert_alpha()
        fondoInicial = pygame.image.load("assets/Fondos/esc2.png").convert_alpha()
    ipapel = pygame.image.load("assets/Items/papel.png").convert_alpha()
    iperiodico = pygame.image.load("assets/Items/periodico.png").convert_alpha()
    ciclista = pygame.image.load("assets/Personajes/NPC/ciclista.png").convert_alpha()
    reloj = pygame.image.load("assets/Items/reloj.png").convert_alpha()
    ipersonaje = pygame.image.load("assets/Personajes/Principal/mov.png").convert_alpha()
    #Calling Classes
    player = Character(life,ipersonaje)
    piedra = Enemy(venemy)
    objeto = Object(vobject1,ipapel)
    objeto2 = Object(vobject2,iperiodico)
    if endgame!=True:
        hilo = threading.Thread(target=crono, args=())
        hilo.start()
    while ss >= tlimit-5:
        ventana.fill(blanco)
        if ss >= tlimit-3:
            ventana.blit(texto2,(200,720/2))
        else:
            if idioma ==True:
                lectura=fuente2.render("¡Listo!",0,(0,0,0))
            if idioma ==False:
                lectura=fuente2.render("Ready!",0,(0,0,0))
            ventana.blit(lectura,(1280/2-200,720/2))
        if idioma ==True:
            lectura=fuente1.render("Presiona espacio para omitir",0,(0,0,0))
        if idioma ==False:
            lectura=fuente1.render("Press space to skip",0,(0,0,0))
        ventana.blit(lectura,(1280/2-200,720-50))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ss = tlimit-6
        ss -=1
        time.sleep(1)
        pygame.display.update()
        seconds = tlimit
    while endgame!=True: #Loop principal
        for event in pygame.event.get(): #Corre todos los eventos en pygame
            if event.type == pygame.QUIT:
                endgame=True
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    controlt = seconds
                    mpause(player,life,juego,music,tlimit,controlt)
                    if seconds == tlimit:
                        piedra.rect.left = 1300
                        objeto.rect.top, objeto.rect.left = randint(160,400), randint(1280,1500)
                        objeto2.rect.top, objeto2.rect.left = randint(160,400), randint(1280,1500)
                        ipersonaje = pygame.image.load("assets/Personajes/Principal/mov.png").convert_alpha()
                        ifondo = fondoInicial
                        if music == True:
                            juego = pygame.mixer.music.play()
                    if seconds == 100:
                        endgame=True
            player.move(event,termino,sound1,sonido)
        if player.salto == True and player.rect.top >= 160 and altlimit == False:
            player.rect.top -=40
        if player.salto == False and player.rect.top < 720/2 and altlimit == False:
            player.rect.top +=40
        if player.rect.top == 120:
            altlimit = True
        if player.rect.top == 720/2:
            altlimit = False
        if altlimit == True and player.rect.top < 720/2:
            player.rect.top += 40
        if player.movei == True and player.rect.left >0:
            player.rect.left -=15
            ipersonaje = pygame.image.load("assets/Personajes/Principal/mov11.png").convert_alpha()
        if player.mover == True and player.rect.left <1200:
            player.rect.left +=15
            ipersonaje = pygame.image.load("assets/Personajes/Principal/mov.png").convert_alpha()
        if fondo==1:
            if seconds<=tlimit/3:
                ifondo = pygame.image.load("assets/Fondos/esc13.png").convert_alpha()
            if seconds<tlimit/3*2 and seconds>tlimit/3:
                ifondo = pygame.image.load("assets/Fondos/esc12.png").convert_alpha()
        if fondo==2:
            if seconds<=tlimit/3:
                ifondo = pygame.image.load("assets/Fondos/esc22.png").convert_alpha()
            if seconds<tlimit/3*2 and seconds>tlimit/3:
                ifondo = pygame.image.load("assets/Fondos/esc21.png").convert_alpha()


        #Chronometer
        if termino == False:
            segundos= str(seconds)

        reloj1.tick(20) #Frame Counter
        #End Game
        if termino == False:
            piedra.collision(player,sound2,sonido)
            objeto.collision(player,5,sound3,sonido)
            objeto2.collision(player,10,sound3,sonido)
            cx -= 20
            if cx <= -1300:
                cx = 1300
        #Draw on the surface
        ventana.blit(ifondo,(0,0))
        ventana.blit(ciclista,(cx,300))
        ventana.blit(reloj,(1125,635))
        player.draw(ventana,ipersonaje)
        player.drawl(ventana,fuente1,idioma)
        player.drawp(ventana,fuente1,idioma)
        ventana.blit(texto1,(50,20))
        chronometer=fuente1.render(segundos,0,(0,0,0))
        ventana.blit(chronometer,(1200,650)) #Draw Chronometer
        piedra.draw(ventana)
        objeto.draw(ventana)
        objeto2.draw(ventana)
        #Lose Condition
        if win == False:
            if player.lifes == 0 or seconds <= 0:
                termino = True
                youlose(player,life,win,sound4,juego,sonido,music,tlimit,idioma)
                if seconds == tlimit:
                    piedra.rect.left = 1300
                    objeto.rect.top, objeto.rect.left = randint(160,400), randint(1280,1500)
                    objeto2.rect.top, objeto2.rect.left = randint(160,400), randint(1280,1500)
                    ipersonaje = pygame.image.load("assets/Personajes/Principal/mov.png").convert_alpha()
                    termino = False
                    ifondo = fondoInicial
                if seconds == 100:
                    endgame=True
                    seconds = 0
        #Win Condition
        if player.points >= pointsg and seconds > 0 or win == True:
            termino = True
            win = True
            youlose(player,life,win,sound5,juego,sonido,music,tlimit,idioma)
            if seconds == tlimit:
                piedra.rect.left = 1300
                objeto.rect.top, objeto.rect.left = randint(160,400), randint(1280,1500)
                objeto2.rect.top, objeto2.rect.left = randint(160,400), randint(1280,1500)
                ipersonaje = pygame.image.load("assets/Personajes/Principal/mov.png").convert_alpha()
                termino = False
                win = False
                ifondo = fondoInicial
            if seconds == 100:
                endgame=True
                seconds = 0
        if endgame == True:
            seconds = 0
        pygame.display.update()


def mpause(player,life,juego,music,tlimit,controlt):
    pygame.init()
    ventana=pygame.display.set_mode([1280,720])
    salir=False
    fuente1 = pygame.font.SysFont ("Arial",30,True,False)
    fuente2 = pygame.font.SysFont ("Arial",60,True,False)
    blanco = (179,19,176)
    reloj1=pygame.time.Clock()
    ifondo = pygame.image.load("assets/Fondos/Pause.png").convert_alpha()
    icontinuar1 = pygame.image.load("assets/Items/continuar.png").convert_alpha()
    icontinuar2 = pygame.image.load("assets/Items/continuar1.png").convert_alpha()
    ireiniciar1 = pygame.image.load("assets/Items/reiniciar.png").convert_alpha()
    ireiniciar2 = pygame.image.load("assets/Items/reiniciar1.png").convert_alpha()
    ihome1 = pygame.image.load("assets/Items/home.png").convert_alpha()
    ihome2 = pygame.image.load("assets/Items/home1.png").convert_alpha()
    cursor1 = Cursor()
    continuar = Button(icontinuar1,icontinuar2,400,720/2-100)
    reiniciar = Button(ireiniciar1,ireiniciar2,720,720/2-100)
    home = Button(ihome1,ihome2,570,720/2+150)
    juego = pygame.mixer.music.pause( )
    while salir!=True: #Loop principal
        for event in pygame.event.get(): #Corre todos los eventos en pygame
            if event.type == pygame.QUIT:
                salir=True
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cursor1.colliderect(continuar.rect):
                global seconds
                seconds = controlt
                player.salto = False
                player.movei = False
                player.mover = False
                salir=True
                juego = pygame.mixer.music.unpause( )
            if cursor1.colliderect(reiniciar.rect):
                seconds = tlimit
                player.points = 0
                player.lifes = life
                player.rect.top = 720/2
                player.rect.left = 1280/2
                player.salto = False
                player.movei = False
                player.mover = False
                salir = True
                juego = pygame.mixer.music.stop()
            if cursor1.colliderect(home.rect):
                seconds = 100
                salir = True
                menu = pygame.mixer.music.load("assets/Sounds/menu.mp3")
                if music == True:
                    menu = pygame.mixer.music.play(3)




        cursor1.update()
        ventana.fill(blanco)
        ventana.blit(ifondo,(200,0))
        continuar.update(ventana,cursor1)
        reiniciar.update(ventana,cursor1)
        home.update(ventana,cursor1)
        pygame.display.update()

def youlose(player,life,win,sound,juego,sonido,music,tlimit,idioma):
    pygame.init()
    ventana=pygame.display.set_mode([1280,720])
    salir=False
    fuente1 = pygame.font.SysFont ("Arial",30,True,False)
    fuente2 = pygame.font.SysFont ("Arial",60,True,False)
    blanco = (255,255,255)
    rojo=(200,20,50)
    verde=(50,205,50)
    reloj1=pygame.time.Clock()
    ifondo = pygame.image.load("assets/Fondos/Pause.png").convert_alpha()
    ireiniciar1 = pygame.image.load("assets/Items/reiniciar.png").convert_alpha()
    ireiniciar2 = pygame.image.load("assets/Items/reiniciar1.png").convert_alpha()
    ihome1 = pygame.image.load("assets/Items/home.png").convert_alpha()
    ihome2 = pygame.image.load("assets/Items/home1.png").convert_alpha()
    cursor1 = Cursor()
    reiniciar = Button(ireiniciar1,ireiniciar2,400,720/2)
    home = Button(ihome1,ihome2,700,720/2)
    juego = pygame.mixer.music.pause()
    if sonido == True:
        sound.play()
    while salir!=True: #Loop principal
        for event in pygame.event.get(): #Corre todos los eventos en pygame
            if event.type == pygame.QUIT:
                salir=True
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(reiniciar.rect):
                    global seconds
                    seconds = tlimit
                    player.points = 0
                    player.lifes = life
                    player.rect.top = 720/2
                    player.rect.left = 1280/2
                    player.salto = False
                    player.movei = False
                    player.mover = False
                    salir = True
                    if music == True:
                        Sjuego = pygame.mixer.music.play()
                if cursor1.colliderect(home.rect):
                    seconds = 100
                    salir = True
                    menu = pygame.mixer.music.load("assets/Sounds/menu.mp3")
                    if music == True:
                        menu = pygame.mixer.music.play(3)
        cursor1.update()
        if win == True:
            ventana.fill(verde)
            player.win(ventana,fuente2,idioma)
        if win == False:
            ventana.fill(rojo)
            player.lose(ventana,fuente2,idioma)
        reiniciar.update(ventana,cursor1)
        home.update(ventana,cursor1)
        pygame.display.update()

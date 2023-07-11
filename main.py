import pygame
import sys
from constantes import *
from player import Player
from auxiliar import *
from plataforma import *
from botin import Botin
from enemigo import Enemy
from score import Score
from tiempo import Tiempo
from lives import Live
from boton import Boton
from portal import Portal

pygame.init()
clock = pygame.time.Clock()

def lvl_1()->None:

    pygame.mixer.music.load(SOUND_LVL_1)
    pygame.mixer.music.play(-1)
    screen_lvl_1 = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    pygame.display.set_caption("Leve 1")
    lista_plataformas_lvl_1 = []
    lista_botin_lvl_1 = []
    lista_enemy_lvl_1 = []

    lista_plataformas_lvl_1.append(Platform(x=0,y=700,width=400,height=100,screen=screen_lvl_1,path=IMAGE_TILTES,type=2))
    lista_plataformas_lvl_1.append(Platform(x=400,y=700,width=100,height=100,screen=screen_lvl_1,path=IMAGE_TILTES,type=3))
    lista_plataformas_lvl_1.append(Platform(x=580,y=700,width=70,height=100,screen=screen_lvl_1,path=IMAGE_TILTES,type=1))
    lista_plataformas_lvl_1.append(Platform(x=650,y=700,width=150,height=100,screen=screen_lvl_1,path=IMAGE_TILTES,type=2))
    lista_plataformas_lvl_1.append(Platform(x=800,y=700,width=50,height=100,screen=screen_lvl_1,path=IMAGE_TILTES,type=3))
    lista_plataformas_lvl_1.append(Platform(x=1300,y=630,width=200,height=70,screen=screen_lvl_1,path=IMAGE_TILTES,type=2))
    lista_plataformas_lvl_1.append(Platform(x=1200,y=700,width=200,height=100,screen=screen_lvl_1,path=IMAGE_TILTES,type=1))
    lista_plataformas_lvl_1.append(Platform(x=1300,y=700,width=200,height=100,screen=screen_lvl_1,path=IMAGE_TILTES,type=2))
    lista_plataformas_lvl_1.append(Platform(x=300,y=600,width=80,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=13))
    lista_plataformas_lvl_1.append(Platform(x=350,y=600,width=80,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=14))
    lista_plataformas_lvl_1.append(Platform(x=400,y=600,width=80,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=15))
    lista_plataformas_lvl_1.append(Platform(x=500,y=530,width=80,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=13))
    lista_plataformas_lvl_1.append(Platform(x=550,y=530,width=80,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=14))
    lista_plataformas_lvl_1.append(Platform(x=600,y=530,width=80,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=15))
    lista_plataformas_lvl_1.append(Platform(x=650,y=450,width=80,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=13))
    lista_plataformas_lvl_1.append(Platform(x=700,y=450,width=80,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=14))
    lista_plataformas_lvl_1.append(Platform(x=750,y=450,width=80,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=15))
    lista_plataformas_lvl_1.append(Platform(x=300,y=440,width=80,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=13))
    lista_plataformas_lvl_1.append(Platform(x=350,y=440,width=80,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=14))
    lista_plataformas_lvl_1.append(Platform(x=400,y=440,width=80,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=15))
    lista_plataformas_lvl_1.append(Platform(x=900,y=650,width=50,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=18))
    lista_plataformas_lvl_1.append(Platform(x=1000,y=650,width=50,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=18))
    lista_plataformas_lvl_1.append(Platform(x=1100,y=650,width=50,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=18))
    lista_plataformas_lvl_1.append(Platform(x=900,y=450,width=50,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=18))
    lista_plataformas_lvl_1.append(Platform(x=1000,y=400,width=50,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=18))
    lista_plataformas_lvl_1.append(Platform(x=1100,y=350,width=50,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=18))
    lista_plataformas_lvl_1.append(Platform(x=1200,y=300,width=50,height=50,screen=screen_lvl_1,path=IMAGE_TILTES,type=18))

    lista_botin_lvl_1.append(Botin(x=320,y=350,w=50,h=50,type=1,filas=1,columnas=17))
    lista_botin_lvl_1.append(Botin(x=370,y=350,w=50,h=50,type=1,filas=1,columnas=17))
    lista_botin_lvl_1.append(Botin(x=420,y=350,w=50,h=50,type=1,filas=1,columnas=17))
    lista_botin_lvl_1.append(Botin(x=900,y=600,w=50,h=50,type=2,filas=1,columnas=17))
    lista_botin_lvl_1.append(Botin(x=1000,y=600,w=50,h=50,type=2,filas=1,columnas=17))
    lista_botin_lvl_1.append(Botin(x=1100,y=600,w=50,h=50,type=2,filas=1,columnas=17))
    lista_botin_lvl_1.append(Botin(x=900,y=400,w=50,h=50,type=3,filas=1,columnas=17))
    lista_botin_lvl_1.append(Botin(x=1000,y=350,w=50,h=50,type=3,filas=1,columnas=17))
    lista_botin_lvl_1.append(Botin(x=1100,y=300,w=50,h=50,type=3,filas=1,columnas=17))
    lista_botin_lvl_1.append(Botin(x=1200,y=250,w=50,h=50,type=3,filas=1,columnas=17))
    
    fondo_lvl_1 = Wallpaper(FONDO_LVL_1,screen_lvl_1,x=0,y=0,w=2,h=5)
    imagen_agua = Wallpaper(FONDO_AGUA,screen_lvl_1,x=10,y=725,w=100,h=50)

    flecha = Boton(x= 10,y=650,w=50,h=50,path=FLECHA_INICIO)
    portal = Portal(x= 1380,y=485,w=150,h=150,frame_rate_ms=5)
   
    lista_enemy_lvl_1.append(Enemy(x=350,y=550,speed_run=40,speed_walk=1,gravity=10,jump_power=10,frame_rate_ms=20,move_rate_ms=50,jump_height=100,p_scale=2,direccion=True))
    lista_enemy_lvl_1.append(Enemy(x=1250,y=650,speed_run=40,speed_walk=1,gravity=10,jump_power=10,frame_rate_ms=20,move_rate_ms=50,jump_height=100,p_scale=2,direccion=True))
    lista_enemy_lvl_1.append(Enemy(x=700,y=400,speed_run=40,speed_walk=1,gravity=10,jump_power=10,frame_rate_ms=20,move_rate_ms=50,jump_height=100,p_scale=2,direccion=False))

    player_1 = Player(x=0,y=550,speed_walk=10,speed_run=40,gravity=15,jump_power=60,interval_time_jump=40,frame_rate_ms=15,jump_height=60)

    life_count = Live(x=1200,y=10,w=50,h=40,live_x=1300,live_y=200,live_w=100,live_h=100)
    scores = Score(x=20,y=10,w=50,h=40)
    tiempo_game = Tiempo(x=600,y=10,w=50,minute=5,second=0)

    jugando_level_1 = True
    while jugando_level_1:
       
        lista_eventos = pygame.event.get()
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        delta_ms = clock.tick(FPS)

        player_1.events(keys,delta_ms)
        fondo_lvl_1.draw(delta_ms) 
        imagen_agua.draw_agua(delta_ms)
        flecha.draw(screen_lvl_1)

        portal.do_animation()
        portal.draw(screen_lvl_1)
 
        if player_1.rect.colliderect(portal.rect_ground_collition):
            pygame.time.delay(1000)
            lvl_2(player_1,scores)
            if DEBUG_PRINT:
                print("Pase de nivel")  

            
        for plataforma in lista_plataformas_lvl_1:
            plataforma.draw()  

        for enemigo in lista_enemy_lvl_1:    
            enemigo.update(delta_ms,lista_plataformas_lvl_1,player_1)
            enemigo.draw(screen_lvl_1)

        for botin in lista_botin_lvl_1:
            botin.do_animation()
            botin.draw(screen_lvl_1)

        life_count.update(player_1)
        life_count.draw(screen_lvl_1)
        
        player_1.update(delta_ms,lista_plataformas_lvl_1,lista_enemy_lvl_1)
        player_1.draw(screen_lvl_1)

        scores.update(player_1,lista_botin_lvl_1)
        scores.draw(screen_lvl_1)

        tiempo_game.update(delta_ms)
        tiempo_game.draw(screen_lvl_1)

        if player_1.lives <= 0:
            game_over()
            if DEBUG_PRINT:
                print("Sin vidas")
                
        if tiempo_game.minute == 0 and tiempo_game.second == 0:
            game_over()        
            if DEBUG_PRINT:
                print("sin tiempo")

        pygame.display.flip()

def lvl_2(player_1,scores)->None:

    pygame.mixer.music.load(SOUND_LVL_2)
    pygame.mixer.music.play(-1)
    screen_lvl_2 = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    pygame.display.set_caption("Leve 2")
    lista_plataformas_lvl_2 = []
    lista_botin_lvl_2 = []
    lista_enemy_lvl_2 = []

    lista_plataformas_lvl_2.append(Platform(x=0,y=700,width=300,height=100,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=2))
    lista_plataformas_lvl_2.append(Platform(x=300,y=700,width=100,height=100,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=3))
    lista_plataformas_lvl_2.append(Platform(x=450,y=700,width=50,height=100,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=2))
    lista_plataformas_lvl_2.append(Platform(x=550,y=700,width=50,height=100,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=2))
    lista_plataformas_lvl_2.append(Platform(x=650,y=700,width=50,height=100,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=2))
    lista_plataformas_lvl_2.append(Platform(x=750,y=700,width=50,height=100,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=2))
    lista_plataformas_lvl_2.append(Platform(x=850,y=700,width=50,height=100,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=2))
    lista_plataformas_lvl_2.append(Platform(x=950,y=700,width=50,height=100,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=2))  
    lista_plataformas_lvl_2.append(Platform(x=1050,y=700,width=50,height=100,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=2))  
    lista_plataformas_lvl_2.append(Platform(x=1150,y=700,width=200,height=100,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=1))
    lista_plataformas_lvl_2.append(Platform(x=1400,y=630,width=100,height=70,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=1))
    lista_plataformas_lvl_2.append(Platform(x=1300,y=700,width=200,height=100,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=2))
    lista_plataformas_lvl_2.append(Platform(x=1180,y=550,width=80,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=14))
    lista_plataformas_lvl_2.append(Platform(x=1230,y=550,width=80,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=15))
    lista_plataformas_lvl_2.append(Platform(x=1280,y=550,width=80,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=16))
    lista_plataformas_lvl_2.append(Platform(x=1380,y=480,width=80,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=14))
    lista_plataformas_lvl_2.append(Platform(x=1430,y=480,width=80,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=15))
    lista_plataformas_lvl_2.append(Platform(x=1480,y=480,width=80,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=16))
    lista_plataformas_lvl_2.append(Platform(x=1380,y=350,width=80,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=14))
    lista_plataformas_lvl_2.append(Platform(x=1430,y=350,width=80,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=15))
    lista_plataformas_lvl_2.append(Platform(x=1480,y=350,width=80,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=16))
    lista_plataformas_lvl_2.append(Platform(x=1180,y=400,width=80,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=14))
    lista_plataformas_lvl_2.append(Platform(x=1230,y=400,width=80,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=15))
    lista_plataformas_lvl_2.append(Platform(x=1280,y=400,width=80,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=16))
    lista_plataformas_lvl_2.append(Platform(x=350,y=430,width=80,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=14))
    lista_plataformas_lvl_2.append(Platform(x=400,y=430,width=80,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=15))
    lista_plataformas_lvl_2.append(Platform(x=450,y=430,width=80,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=16))
    lista_plataformas_lvl_2.append(Platform(x=900,y=450,width=50,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=18))
    lista_plataformas_lvl_2.append(Platform(x=1000,y=500,width=50,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=18))
    lista_plataformas_lvl_2.append(Platform(x=1100,y=450,width=50,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=18))
    lista_plataformas_lvl_2.append(Platform(x=800,y=400,width=50,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=18))
    lista_plataformas_lvl_2.append(Platform(x=685,y=450,width=50,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=18))
    lista_plataformas_lvl_2.append(Platform(x=570,y=430,width=50,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=18))
    lista_plataformas_lvl_2.append(Platform(x=250,y=400,width=50,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=18))
    lista_plataformas_lvl_2.append(Platform(x=170,y=330,width=50,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=18))
    lista_plataformas_lvl_2.append(Platform(x=1340,y=250,width=50,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=18)) 
    lista_plataformas_lvl_2.append(Platform(x=400,y=200,width=200,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=14))
    lista_plataformas_lvl_2.append(Platform(x=600,y=200,width=500,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=15))
    lista_plataformas_lvl_2.append(Platform(x=1100,y=200,width=200,height=50,screen=screen_lvl_2,path=IMAGE_TILTES_2,type=16))
   
    lista_botin_lvl_2.append(Botin(x=450,y=600,w=50,h=50,type=8,filas=1,columnas=17))
    lista_botin_lvl_2.append(Botin(x=550,y=600,w=50,h=50,type=8,filas=1,columnas=17))
    lista_botin_lvl_2.append(Botin(x=650,y=600,w=50,h=50,type=8,filas=1,columnas=17))
    lista_botin_lvl_2.append(Botin(x=760,y=600,w=50,h=50,type=8,filas=1,columnas=17))
    lista_botin_lvl_2.append(Botin(x=850,y=600,w=50,h=50,type=8,filas=1,columnas=17))
    lista_botin_lvl_2.append(Botin(x=950,y=600,w=50,h=50,type=8,filas=1,columnas=17))
    lista_botin_lvl_2.append(Botin(x=1050,y=600,w=50,h=50,type=8,filas=1,columnas=17))
    lista_botin_lvl_2.append(Botin(x=250,y=350,w=50,h=50,type=9,filas=1,columnas=17))
    lista_botin_lvl_2.append(Botin(x=570,y=380,w=50,h=50,type=9,filas=1,columnas=17))
    lista_botin_lvl_2.append(Botin(x=685,y=400,w=50,h=50,type=9,filas=1,columnas=17))
    lista_botin_lvl_2.append(Botin(x=800,y=340,w=50,h=50,type=9,filas=1,columnas=17))
    lista_botin_lvl_2.append(Botin(x=900,y=390,w=50,h=50,type=9,filas=1,columnas=17))
    lista_botin_lvl_2.append(Botin(x=1000,y=440,w=50,h=50,type=9,filas=1,columnas=17))
    lista_botin_lvl_2.append(Botin(x=1100,y=390,w=50,h=50,type=9,filas=1,columnas=17))
    
    life_count = Live(x=1200,y=10,w=50,h=40,live_x=140,live_y=250,live_w=100,live_h=100)
    
    player_1.restart()
    flecha = Boton(x= 10,y=650,w=50,h=50,path=FLECHA_INICIO)
    lista_enemy_lvl_2.append(Enemy(x=900,y=150,speed_run=40,speed_walk=1,gravity=10,jump_power=10,frame_rate_ms=50,move_rate_ms=50,jump_height=100,p_scale=2,direccion=True))
    lista_enemy_lvl_2.append(Enemy(x=700,y=150,speed_run=40,speed_walk=1,gravity=10,jump_power=10,frame_rate_ms=50,move_rate_ms=50,jump_height=100,p_scale=2,direccion=False))
    lista_enemy_lvl_2.append(Enemy(x=400,y=380,speed_run=40,speed_walk=1,gravity=10,jump_power=10,frame_rate_ms=50,move_rate_ms=50,jump_height=100,p_scale=2,direccion=True))

    tiempo_game = Tiempo(x=600,y=10,w=50,minute=5,second=0)

    portal = Portal(x= 370,y=60,w=150,h=150,frame_rate_ms=5)

    fondo_lvl_2 = Wallpaper(FONDO_LVL_2,screen_lvl_2,x=0,y=0,w=3,h=5)
    fondo_agua = Wallpaper(FONDO_AGUA,screen_lvl_2,x=10,y=725,w=100,h=100)

    jugando_level_1 = True
    while jugando_level_1:
       
        lista_eventos = pygame.event.get()
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        delta_ms = clock.tick(FPS)

        player_1.events(keys,delta_ms)

        fondo_lvl_2.draw(delta_ms) 
        flecha.draw(screen_lvl_2)
        fondo_agua.draw_agua(delta_ms)

        portal.do_animation()
        portal.draw(screen_lvl_2)

        if player_1.rect.colliderect(portal.rect_ground_collition):
            win(player_1,scores)
            if DEBUG_PRINT:
                print("Gane el juego")
        
        for botin in lista_botin_lvl_2 :
            botin.do_animation()
            botin.draw(screen_lvl_2)

        for plataforma in lista_plataformas_lvl_2:
            plataforma.draw()  

        for enemigo in lista_enemy_lvl_2:    
            enemigo.update(delta_ms,lista_plataformas_lvl_2,player_1)
            enemigo.draw(screen_lvl_2)

        

        life_count.update(player_1)
        life_count.draw(screen_lvl_2)
        
        player_1.update(delta_ms,lista_plataformas_lvl_2,lista_enemy_lvl_2)
        player_1.draw(screen_lvl_2)

        scores.update(player_1,lista_botin_lvl_2)
        scores.draw(screen_lvl_2)

        tiempo_game.update(delta_ms)
        tiempo_game.draw(screen_lvl_2)

        if player_1.lives <= 0:
            jugando_level_1  = False
            if DEBUG_PRINT:
                print("Sin vidas ")
                
        if tiempo_game.minute == 0 and tiempo_game.second == 0: 
            if DEBUG_PRINT:
                print("sin tiempo")

        
        pygame.display.flip()

def menu()->None:

    pygame.mixer.music.load(SOUND_MENU)
    pygame.mixer.music.play()
    screen_menu = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    pygame.display.set_caption("Menu")

    fondo_menu = pygame.image.load(FONDO_MENU)
    fondo_menu_scale = pygame.transform.scale(fondo_menu,(ANCHO_VENTANA,ALTO_VENTANA))
    screen_menu.blit(fondo_menu_scale,fondo_menu_scale.get_rect())


    fondo = Platform(x= 488,y=520,width=600,height=200,screen=screen_menu,path="images\mi_menu",type=6)
    titulo = Platform(x= 430,y=90,width=700,height=250,screen=screen_menu,path="images\mi_menu",type=10)
    fuente = pygame.font.Font(None, 100)
    texto_titulo = fuente.render("Panchii ",True,BLACK)

    boton_play = Boton(x= 530,y=550,w=150,h=150,path="images\mi_menu\\4.png")
    boton_setting = Boton(x= 710,y=550,w=150,h=150,path="images\mi_menu\\5.png")
    boton_info = Boton(x= 890,y=550,w=150,h=150,path="images\mi_menu\\7.png")
   

    mostrando_menu = True
    while mostrando_menu:

        lista_eventos = pygame.event.get()
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        fondo.draw()
        titulo.draw()
       
        boton_play.draw(screen_menu)
        boton_setting.draw(screen_menu)
        boton_info.draw(screen_menu)

        if boton_play.click():
            lvl_1()
        elif boton_setting.click():
            setting()
        elif boton_info.click():
            info()
        
        

        screen_menu.blit(texto_titulo,(650,160))
        pygame.display.flip()

def setting()->None:
    
    sound = False
    screen_setting = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    fondo_setting = pygame.image.load(FONDO_SETTING)
    fondo_setting_scale = pygame.transform.scale(fondo_setting,(ANCHO_VENTANA,ALTO_VENTANA))
    screen_setting.blit(fondo_setting_scale,fondo_setting_scale.get_rect())

    fondo = Platform(x= 450,y=65,width=700,height=700,screen=screen_setting,path="images\setting",type=1)
    titulo = Platform(x= 480,y=80,width=650,height=300,screen=screen_setting,path="images\setting",type=2)

    boton_sound_play = Boton(x= 860,y=350,w=100,h=100,path="images\mi_menu\\9.png")
    boton_sound_stop = Boton(x= 960,y=350,w=100,h=100,path="images\mi_menu\\8.png")
    boton_prew =  Boton(x= 510,y=350,w=100,h=100,path=PREW_SETTING)

    boton_volumen_menor = Boton(x= 910,y=500,w=50,h=50,path="images\setting\\3.png")
    boton_volumen_mayor = Boton(x= 1010,y=500,w=50,h=50,path="images\setting\\4.png")

    boton_fps_menor = Boton(x= 910,y=600,w=50,h=50,path="images\setting\\3.png")
    boton_fps_mayor = Boton(x= 1010,y=600,w=50,h=50,path="images\setting\\4.png")

    fuente = pygame.font.Font(None, 60)
    texto_surface_volumen = fuente.render("Ajuste de volumen",True,BLACK)
    texto_surface_fps = fuente.render("Ajuste de FPS" ,True,BLACK)


    mostrar_setting = True
    while mostrar_setting:
        lista_eventos = pygame.event.get()
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        fondo.draw()
        titulo.draw()
        boton_prew.draw(screen_setting)
        boton_sound_play.draw(screen_setting)
        boton_sound_stop.draw(screen_setting)
        boton_volumen_menor.draw(screen_setting)
        boton_volumen_mayor.draw(screen_setting)
        boton_fps_menor.draw(screen_setting)
        boton_fps_mayor.draw(screen_setting)
        

        if boton_prew.click():
            menu()

        if boton_sound_play.click() and sound:
            pygame.mixer.music.set_volume(V_50)
        elif boton_sound_stop.click():
            pygame.mixer.music.set_volume(V_0)
            sound = True
        elif boton_volumen_menor.click():
            pygame.mixer.music.set_volume(V_25)
        elif boton_volumen_mayor.click():
             pygame.mixer.music.set_volume(V_100)
        elif boton_fps_menor.click():
            FPS = FPS_MITAD
            print(FPS)
        elif boton_fps_mayor.click():
            FPS = FPS_DOBLE
            print(FPS)

        screen_setting.blit(texto_surface_volumen,(510,500))
        screen_setting.blit(texto_surface_fps,(510,600))
        pygame.display.flip()

def game_over()->None:
    
    pygame.mixer.music.load(SOUND_GAME_OVER)
    
    music_on = True
    if music_on:
        pygame.mixer.music.play()
        music_on = False
    else:
        pygame.mixer.music.stop()
        

    screen_game_over = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    pygame.display.set_caption("GAME OVER")
    fondo_game_over = pygame.image.load(FONDO_SETTING)
    fondo_game_over_scale = pygame.transform.scale(fondo_game_over,(ANCHO_VENTANA,ALTO_VENTANA))
    screen_game_over.blit(fondo_game_over_scale,fondo_game_over_scale.get_rect())

    fondo = Platform(x= 450,y=65,width=700,height=700,screen=screen_game_over,path="images\game_over",type=1)
    titulo = Platform(x= 480,y=80,width=650,height=300,screen=screen_game_over,path="images\game_over",type=2)
    boton_prew =  Boton(x= 510,y=350,w=100,h=100,path=PREW_SETTING)

    mostar_game_over = True
    while mostar_game_over:

        lista_eventos = pygame.event.get()
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        fondo.draw()
        titulo.draw()

        if boton_prew.click():
            menu()


        boton_prew.draw(screen_game_over)

        pygame.display.flip()

def info()->None:

    screen_info = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    fondo_setting = pygame.image.load(FONDO_INFO)

    pygame.mixer.music.set_volume(V_0)
    fondo_game_over_scale = pygame.transform.scale(fondo_setting,(ANCHO_VENTANA,ALTO_VENTANA))
    screen_info.blit(fondo_game_over_scale,fondo_game_over_scale.get_rect())

    boton_prew =  Boton(x= 50,y=50,w=50,h=50,path=PREW_SETTING)

    fuente = pygame.font.Font(None, 70)
    texto_nombre = fuente.render("Creado por: Pablo Andrada.",True,SKY_BLUE)
  
    mostar_info = True
    while mostar_info:

        lista_eventos = pygame.event.get()
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if boton_prew.click():
            pygame.mixer.music.set_volume(V_50)
            menu()


        boton_prew.draw(screen_info)
        screen_info.blit(texto_nombre,(50,500))
        pygame.display.flip()

def win(player_1,scores):

    screen_win = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    pygame.display.set_caption("GAME OVER")
    fondo_win = pygame.image.load(FONDO_SETTING)
    fondo_win_scale = pygame.transform.scale(fondo_win,(ANCHO_VENTANA,ALTO_VENTANA))
    screen_win.blit(fondo_win_scale,fondo_win_scale.get_rect())

    fondo = Platform(x= 450,y=65,width=700,height=700,screen=screen_win,path="images\game_over",type=1)
    #titulo = Platform(x= 480,y=80,width=650,height=300,screen=screen_win,path="images\game_over",type=2)
    boton_prew =  Boton(x= 510,y=250,w=100,h=100,path=PREW_SETTING)


    fuente = pygame.font.Font(None, 70)
    texto_live = fuente.render("Live: {0}".format(player_1.lives),True,SKY_BLUE)
    texto_score = fuente.render("Score: {0}".format(scores.score),True,SKY_BLUE)
  
  
    mostar_info = True
    while mostar_info:

        lista_eventos = pygame.event.get()
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        fondo.draw()
        if boton_prew.click():
            pygame.mixer.music.set_volume(V_50)
            menu()

        boton_prew.draw(screen_win)
        screen_win.blit(texto_live,(500,500))
        screen_win.blit(texto_score,(500,600))
        pygame.display.flip()


start_menu = True
jugando = True
while jugando:
    

    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)
    
    if start_menu:
        game_menu = False
        menu()
    

    pygame.display.flip()

    

   



    







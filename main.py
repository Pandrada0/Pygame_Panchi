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
import json


def leer_json(data : str) -> list:
    '''load the information from a json to a list
    param: a path of an archive json
    return: a list of pokemons'''
    with open(data,"r") as file_object:
        lista_lvls = json.load(file_object)
        lista_lvls = lista_lvls["Game"]
        return lista_lvls


lista_lvls = leer_json("data.json")

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

    for plataforma in lista_lvls["lvl1"]["plataforma"]:
        lista_plataformas_lvl_1.append(Platform(plataforma["x"],plataforma["y"],plataforma["width"],plataforma["height"],screen_lvl_1,IMAGE_TILTES_1,plataforma["type"]))
    
    for botin in lista_lvls["lvl1"]["botin"]:
        lista_botin_lvl_1.append(Botin(botin["x"],botin["y"],botin["w"],botin["h"],botin["type"],botin["filas"],botin["columnas"]))
 
    for enemigo in lista_lvls["lvl1"]["enemigo"]:
        lista_enemy_lvl_1.append(Enemy(enemigo["x"],enemigo["y"],enemigo["speed_walk"],enemigo["speed_run"],enemigo["gravity"],enemigo["jump_power"],enemigo["frame_rate_ms"],enemigo["move_rate_ms"],enemigo["jump_height"],enemigo["p_scale"],enemigo["direccion"]))
  
    fondo_lvl_1 = Wallpaper(FONDO_LVL_1,screen_lvl_1,x=0,y=0,w=2,h=5)
    imagen_agua_move = Wallpaper(FONDO_AGUA,screen_lvl_1,x=10,y=725,w=100,h=50)

    flecha = Boton(x= 10,y=650,w=50,h=50,path=FLECHA_INICIO)
    portal = Portal(x= 1380,y=485,w=150,h=150,frame_rate_ms=5)
   
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
        imagen_agua_move.draw_agua(delta_ms)
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


    for plataforma in lista_lvls["lvl2"]["plataforma"]:
        lista_plataformas_lvl_2.append(Platform(plataforma["x"],plataforma["y"],plataforma["width"],plataforma["height"],screen_lvl_2,IMAGE_TILTES_2,plataforma["type"]))
    
    for botin in lista_lvls["lvl2"]["botin"]:
        lista_botin_lvl_2.append(Botin(botin["x"],botin["y"],botin["w"],botin["h"],botin["type"],botin["filas"],botin["columnas"]))
 
    for enemigo in lista_lvls["lvl2"]["enemigo"]:
        lista_enemy_lvl_2.append(Enemy(enemigo["x"],enemigo["y"],enemigo["speed_walk"],enemigo["speed_run"],enemigo["gravity"],enemigo["jump_power"],enemigo["frame_rate_ms"],enemigo["move_rate_ms"],enemigo["jump_height"],enemigo["p_scale"],enemigo["direccion"]))


    life_count = Live(x=1200,y=10,w=50,h=40,live_x=140,live_y=250,live_w=100,live_h=100)
    player_1.restart()
    flecha = Boton(x= 10,y=650,w=50,h=50,path=FLECHA_INICIO)
    tiempo_game = Tiempo(x=600,y=10,w=50,minute=5,second=0)
    portal = Portal(x= 370,y=60,w=150,h=150,frame_rate_ms=5)
    fondo_lvl_2 = Wallpaper(FONDO_LVL_2,screen_lvl_2,x=0,y=0,w=3,h=5)
    fondo_agua = Wallpaper(FONDO_AGUA,screen_lvl_2,x=10,y=725,w=100,h=100)

    jugando_level_2 = True
    while jugando_level_2:
       
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
            lvl_3()
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
            game_over()
            if DEBUG_PRINT:
                print("Sin vidas ")
                
        if tiempo_game.minute == 0 and tiempo_game.second == 0: 
            game_over()
            if DEBUG_PRINT:
                print("sin tiempo")
        
        pygame.display.flip()

def lvl_3(player_1,scores)->None:

    pygame.mixer.music.load(SOUND_LVL_3)
    pygame.mixer.music.play(-1)
    screen_lvl_3 = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    pygame.display.set_caption("Leve 3")
    lista_plataformas_lvl_3 = []
    lista_botin_lvl_3 = []
    lista_enemy_lvl_3 = []


    for plataforma in lista_lvls["lvl3"]["plataforma"]:
        lista_plataformas_lvl_3.append(Platform(plataforma["x"],plataforma["y"],plataforma["width"],plataforma["height"],screen_lvl_3,IMAGE_TILTES_3,plataforma["type"]))
    
    for botin in lista_lvls["lvl3"]["botin"]:
        lista_botin_lvl_3.append(Botin(botin["x"],botin["y"],botin["w"],botin["h"],botin["type"],botin["filas"],botin["columnas"]))
 
    for enemigo in lista_lvls["lvl3"]["enemigo"]:
        lista_enemy_lvl_3.append(Enemy(enemigo["x"],enemigo["y"],enemigo["speed_walk"],enemigo["speed_run"],enemigo["gravity"],enemigo["jump_power"],enemigo["frame_rate_ms"],enemigo["move_rate_ms"],enemigo["jump_height"],enemigo["p_scale"],enemigo["direccion"]))


    

    life_count = Live(x=1200,y=10,w=50,h=40,live_x=140,live_y=250,live_w=100,live_h=100)
    player_1.restart()
    flecha = Boton(x= 10,y=650,w=50,h=50,path=FLECHA_INICIO)
    tiempo_game = Tiempo(x=600,y=10,w=50,minute=2,second=0)
    portal = Portal(x= 980,y=150,w=150,h=150,frame_rate_ms=5)

    fondo_lvl_3 = Wallpaper(FONDO_LVL_3,screen_lvl_3,x=0,y=0,w=3,h=5)
    fondo_agua_move = Wallpaper(FONDO_AGUA,screen_lvl_3,x=10,y=725,w=100,h=50)

    jugando_level_3 = True
    while jugando_level_3:
       
        lista_eventos = pygame.event.get()
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        delta_ms = clock.tick(FPS)

        player_1.events(keys,delta_ms)

        fondo_lvl_3.draw(delta_ms) 
        flecha.draw(screen_lvl_3)
    
        portal.do_animation()
        portal.draw(screen_lvl_3)

        if player_1.rect.colliderect(portal.rect_ground_collition):
            win(player_1,scores)
            if DEBUG_PRINT:
                print("Gane el juego")
        
        for botin in lista_botin_lvl_3 :
            botin.do_animation()
            botin.draw(screen_lvl_3)

        for plataforma in lista_plataformas_lvl_3:
            plataforma.draw()  

        for enemigo in lista_enemy_lvl_3:    
            enemigo.update(delta_ms,lista_plataformas_lvl_3,player_1)
            enemigo.draw(screen_lvl_3)

        
        life_count.update(player_1)
        life_count.draw(screen_lvl_3)
        
        player_1.update(delta_ms,lista_plataformas_lvl_3,lista_enemy_lvl_3)
        player_1.draw(screen_lvl_3)

        scores.update(player_1,lista_botin_lvl_3)
        scores.draw(screen_lvl_3)

        tiempo_game.update(delta_ms)
        tiempo_game.draw(screen_lvl_3)

        if player_1.lives <= 0:
            game_over()
            if DEBUG_PRINT:
                print("Sin vidas ")
                
        if tiempo_game.minute == 0 and tiempo_game.second == 0: 
            game_over()
            if DEBUG_PRINT:
                print("sin tiempo")

        fondo_agua_move.draw_agua(delta_ms)
       
        
        #fondo_agua_2.draw_agua(delta_ms,True)

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

def nombre():
    pygame.init()

    screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption('user input')

    user_ip = ''
    font = pygame.font.SysFont('frenchscript',40)
    text_box = pygame.Rect(75,75,100,50)
    active = False
    color = pygame.Color('purple')
    clock = pygame.time.Clock()

    boton_play = Boton(x= 50,y=200,w=150,h=150,path="images\mi_menu\\4.png")
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
            if events.type == pygame.MOUSEBUTTONDOWN:
                if text_box.collidepoint(events.pos):
                    active = True
                else:
                    active = False
            if events.type == pygame.KEYDOWN:
                if active:
                    if events.key == pygame.K_BACKSPACE:
                        user_ip = user_ip[:-1]
                    else:
                        user_ip += events.unicode

        screen.fill('pink')
        if active:
            color = pygame.Color('red')
        else:
            color = pygame.Color('purple')

            if boton_play.click():
                print(user_ip)

        boton_play.draw(screen)
        pygame.draw.rect(screen,color, text_box,4)
        surf = font.render(user_ip,True,'orange')
        screen.blit(surf, (text_box.x +5 , text_box.y +5))
        text_box.w = max(100, surf.get_width()+10)
        pygame.display.update()
        clock.tick(50)


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

    

   



    







import pygame
from constantes import *
from auxiliar import Auxiliar
from botin import Botin
from score import Score
from tiempo import Tiempo
from plataforma import Platform

class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,interval_time_jump,frame_rate_ms,jump_height) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images\Virtual Guy\Run.png",12,1)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images\Virtual Guy\Run.png",12,1,True)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images\Virtual Guy\Idle.png",11,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images\Virtual Guy\Idle.png",11,1,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("images\Virtual Guy\Jump.png",1,1,)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("images\Virtual Guy\Jump.png",1,1,True)
        self.dead =  Auxiliar.getSurfaceFromSpriteSheet("images\Virtual Guy\Hit.png",7,1)
        self.frame = 0
        self.lives = 3
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.direction = DIRECTION_R
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.image = pygame.transform.scale(self.animation[self.frame],(ANCHO_PLAYER,ALTO_PLAYER))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frame_rate_ms = frame_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w /3, self.rect.y + self.rect.h - GROUND_RECT_H , self.rect.w / 3, GROUND_RECT_H)
        

        self.sound_live = pygame.mixer.Sound(SOUND_VIDA)
        self.sound_jump = pygame.mixer.Sound(SOUND_PLAYER_SALTO)
        self.sound_score =  pygame.mixer.Sound(SOUND_FRUTAS)
        self.sound_dead = pygame.mixer.Sound(SOUND_PLAYER_MUERTE)
        self.sound_game_over = pygame.mixer.Sound(SOUND_GAME_OVER)
        self.sound_ive =  pygame.mixer.Sound(SOUND_VIDA)


        self.is_jump = False
        self.is_fall = False
        self.is_plataforma_move = False
        self.is_animation  = False

        self.tiempo_transcurrido = 0
        self.tiempo_transcurrido_animation = 0
        self.tiempo_transcurrido_move = 0
        self.tiempo_last_jump = 0
        self.interval_time_jump = interval_time_jump

    def walk(self,direction):
        
        if  self.direction != direction or (self.animation != self.walk_r  and 
                                            self.animation != self.walk_l):
            self.frame = 0
            self.direction = direction
            if direction == DIRECTION_R :
                self.move_x = self.speed_walk
                self.animation = self.walk_r        
                if DEBUG_PRINT: 
                    print("Movimiento hacia la derecha")
            
            else: 
                self.move_x = -self.speed_walk
                self.animation = self.walk_l
                if DEBUG_PRINT:
                    print("Movimiento hacia la Izquierda")
        
    def events(self,keys,delta_ms):
        self.tiempo_transcurrido += delta_ms
        
        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_R)

        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_L)

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] ):
            self.stay()
        
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] ):
            self.stay()  
    
        if(keys[pygame.K_SPACE]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido

    def jump(self,on_off = False):

        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = int(self.speed_walk/4)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
                if DEBUG_PRINT:
                    print("Salta hacia la derecha")
            else:
                self.move_x = int(self.speed_walk/4)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
                if DEBUG_PRINT:
                    print("Salta hacia la izquierda")
            self.frame = 0
            self.is_jump = True
            volumen_actual = pygame.mixer.music.get_volume()
            if DEBUG_SOUND:
                pygame.mixer.music.get_volume(0.0)
            elif volumen_actual >= V_25:
                self.sound_jump.play()
       
        if on_off == False :
            self.is_jump = False
            self.stay()

    def stay(self):
       
       if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def do_move(self,delta_ms,lista_plataforma,lista_enemy_lvl_1):
        self.tiempo_transcurrido_move += delta_ms
        
        if self.tiempo_transcurrido_move >= self.frame_rate_ms:
            if abs(self.y_start_jump) - abs(self.rect.y) > self.jump_height and self.is_jump:
                self.move_y = 0
            self.tiempo_transcurrido_move = 0  

            if (self.direction == DIRECTION_L and self.rect.x >= 0) or \
                (self.direction == DIRECTION_R and self.rect.x <= ANCHO_VENTANA - self.rect.width): 
                self.add_x(self.move_x)             
            self.add_y(self.move_y)
                
            if (not self.is_on_platfom(lista_plataforma,lista_enemy_lvl_1)) and self.rect.y > ALTO_VENTANA -10:
                self.restart()   
                self.get_hit()

            if(not self.is_on_platfom(lista_plataforma,lista_enemy_lvl_1)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.add_y(self.gravity)

            else:
                if (self.is_jump): 
                    self.jump(False) 

                self.is_fall = False  

    def is_on_platfom(self,lista_plataforma,lista_enemy_lvl_1):
        retorno = False
        
        for plataforma in lista_plataforma:
            if self.rect_ground_collition.colliderect(plataforma.rect_ground_collition) :
                retorno = True
                break  

        for enemigo in lista_enemy_lvl_1:

            if self.rect_ground_collition.colliderect(enemigo.rect_collition_side) and  (enemigo.lives == 3 or enemigo.is_live):
                self.restart()
                self.get_hit()
                retorno = True
                if DEBUG_PRINT:
                    print("descontamos una vida")
                
        return retorno

    def restart(self):  
        self.rect.x = 0
        self.rect.y = GROUND_LEVEL
        self.rect_ground_collition.x =  self.rect.x + self.rect.w / 4
        self.rect_ground_collition.y = self.rect.y + self.rect.h - GROUND_RECT_H

    def add_x (self,delta_x):        
        self.rect.x += delta_x
        self.rect_ground_collition.x += delta_x
        
    def add_y (self,delta_y):
        self.rect.y += delta_y
        self.rect_ground_collition.y  += delta_y


    def do_animation(self,delta_ms):   
        self.tiempo_transcurrido_animation += delta_ms
        
        if self.tiempo_transcurrido_animation >= self.frame_rate_ms or not self.is_animation:
            self.tiempo_transcurrido_animation = 0
            self.is_animation = True
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0    
   
    def get_hit(self):
        self.animation = self.dead
        self.frame = 0
        self.lives -= 1
        self.restart() 
        volumen_actual = pygame.mixer.music.get_volume()
        if DEBUG_SOUND:
            pygame.mixer.music.get_volume(0.0)
        elif volumen_actual >= V_25:
            self.sound_dead.play()

        print("Volumen actual:", volumen_actual)
        
        if DEBUG_PRINT:
            print("descontamos una vida al player",self.lives)

    def update(self,delta_ms,lista_plataforma,lista_enemy_lvl_1):
        self.do_move(delta_ms,lista_plataforma,lista_enemy_lvl_1)
        self.do_animation(delta_ms)

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect,2)
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition,2)
  
        self.image = self.animation[self.frame]
        self.image = pygame.transform.scale(self.image,(ANCHO_PLAYER,ALTO_PLAYER))
        screen.blit(self.image,self.rect)
       
        





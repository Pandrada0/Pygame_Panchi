from player import *
from constantes import *
from auxiliar import Auxiliar

class Enemy():
    
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100,direccion=None) -> None:
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images\Snail\Walk (38x24).png",10,1,False,step=1,scale=p_scale)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images\Snail\Walk (38x24).png",10,1,True,step=1,scale=p_scale)
        self.idle_l = Auxiliar.getSurfaceFromSpriteSheet("images\Snail\Shell Idle (38x24).png",6,1,False,step=1,scale=p_scale)
        self.idle_r = Auxiliar.getSurfaceFromSpriteSheet("images\Snail\Shell Idle (38x24).png",6,1,True,step=1,scale=p_scale)
    
        self.contador_izq = 0
        self.contador_der = 0
        self.frame = 0
        self.lives = 3
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.walk_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x,y,self.rect.w,self.rect.h)

        self.rect_ground_collition = pygame.Rect( self.rect.x, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w, GROUND_RECT_H)
        self.rect_collition_enemy = pygame.Rect(self.rect.x + GROUND_RECT_W*2, y + self.rect.h/3  - GROUND_RECT_H ,self.rect.w /2 + GROUND_RECT_W,self.rect.h - GROUND_RECT_H )
        self.rect_collition_side  = pygame.Rect(self.rect.x + GROUND_RECT_H, self.rect.y + 30,self.rect.w - GROUND_RECT_W*2 ,GROUND_RECT_H *3)

        self.is_direction = direccion
        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False
        self.is_live = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_dead = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 
        self.interval_time_jump = interval_time_jump
   
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.rect_ground_collition.x += delta_x
        self.rect_collition_enemy.x += delta_x
        self.rect_collition_side.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.rect_ground_collition.y += delta_y
        self.rect_collition_enemy.y += delta_y
        self.rect_collition_side.y += delta_y     

    def do_movement(self,delta_ms,plataform_list,player_1):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move -= self.tiempo_transcurrido_move 
            
            if self.lives == 3:
                self.change_x(self.move_x)
                if self.is_direction:
                    if self.contador_izq <= 50 :
                        self.move_x = -self.speed_walk
                        self.direction = DIRECTION_L
                        self.animation = self.walk_l
                        self.contador_izq += 1 
                    elif self.contador_izq <= 100 :
                        self.move_x = self.speed_walk
                        self.direction = DIRECTION_R
                        self.animation = self.walk_r
                        self.contador_izq += 1
                    else:
                        self.contador_izq = 0
                else:
                    if self.contador_der <= 40 :
                        self.move_x = self.speed_walk
                        self.direction = DIRECTION_R
                        self.animation = self.walk_r
                        self.contador_der += 1 
                    elif self.contador_der <= 80 :
                        self.move_x = -self.speed_walk
                        self.direction = DIRECTION_L
                        self.animation = self.walk_l
                        self.contador_der += 1
                    else:
                        self.contador_der = 0

            elif self.lives == 2: 
                if self.direction == DIRECTION_R:
                    self.animation = self.idle_r
                elif self.direction == DIRECTION_L:
                    self.animation = self.idle_l
                self.move_x = 0
                self.move_y = 0   
                
            
            elif self.lives < 0 or self.is_live:
                self.bounce(delta_ms)

            if(not self.is_on_plataform(plataform_list,player_1) ):
                self.change_y(self.gravity)
                
    def bounce(self,delta_ms):    
        self.tiempo_transcurrido_dead += delta_ms

        if self.rect.x >= ANCHO_VENTANA - 10:
            self.animation = self.idle_l
            self.direction = DIRECTION_L
            self.speed_run = -self.speed_run

        elif  self.rect.x <= 0 and self.direction == DIRECTION_L:
            self.animation = self.idle_r
            self.direction = DIRECTION_R
            self.speed_run = -self.speed_run                  
        self.change_x(self.speed_run)      
        
        if self.tiempo_transcurrido_dead >= 1000: 
            self.is_live = True 

    def is_on_plataform(self,plataform_list,player_1):
        retorno = False      
        for plataforma in  plataform_list:
            if(self.rect_ground_collition.colliderect(plataforma.rect_ground_collition)):
                retorno = True
                break  

        if self.rect_collition_enemy.colliderect(player_1.rect_ground_collition):
            self.get_hit()   
            if self.direction == DIRECTION_R :
                    self.animation = self.idle_r 
                    if DEBUG_PRINT:
                        print("colicion R")
            elif self.direction == DIRECTION_L :
                    self.animation = self.idle_l 
                    if DEBUG_PRINT:
                        print("colicion L")
            retorno = True
        return retorno           

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                
            else: 
                self.frame = 0

    def get_hit(self):
        self.lives -= 1
        if DEBUG_PRINT:
           print("descontamos una vida al enemigo",self.lives)

    def update(self,delta_ms,plataform_list,player_1):
        self.do_movement(delta_ms,plataform_list,player_1)
        self.do_animation(delta_ms) 

    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,(255,0 ,0),self.collition_rect,2)
            pygame.draw.rect(screen,(255,255,0),self.rect_ground_collition,2) # piso
            pygame.draw.rect(screen,(255,255,255),self.rect_collition_enemy,2) # dead
            pygame.draw.rect(screen,(0,255,255),self.rect_collition_side)
            


        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        
        

        

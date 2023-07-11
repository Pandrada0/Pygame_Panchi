import pygame
from constantes import *
from auxiliar import Auxiliar


class Platform:

    def __init__(self,x,y,width,height,screen,path,type) -> None:

        self.image = pygame.image.load("{0}\\{1}.png".format(path,type))
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_x = 0
        self.move_y = 0
        self.elapsed_time = 0
        self.screen = screen
        self.rect_ground_collition = pygame.Rect(self.rect.x,self.rect.y, self.rect.w , GROUND_RECT_H )
        self.is_move = False

    def draw(self):
        self.screen.blit(self.image,(self.rect.x , self.rect.y )) 
        if(DEBUG):
            pygame.draw.rect(self.screen,GREEN,self.rect)
            pygame.draw.rect(self.screen,RED,self.rect_ground_collition)

class Wallpaper:

    def __init__(self,path,screen,x=0,y=0,w=0,h=0):
        
        self.image = pygame.image.load(path)
        self.fotograma_ancho = int(self.image.get_width())
        self.fotograma_alto = int(self.image.get_height())
        self.background_y = -125
        self.background_x = -126
        self.x = x
        self.y = y
        self.screen = screen
        self.rep_count_x = ANCHO_VENTANA // self.fotograma_ancho + h
        self.rep_count_y = ALTO_VENTANA // self.fotograma_alto + w
        self.time_elapsed = 0
        self.time_interval = 100
        
    def draw(self,delta_ms):
            self.time_elapsed += delta_ms
            if self.time_elapsed > self.time_interval:
                self.time_elapsed -= self.time_interval
        
            for x in range(self.rep_count_x):            
                for y in range(self.rep_count_y):
                    self.screen.blit(self.image, (x * self.fotograma_ancho, y * self.fotograma_alto + self.background_y ))                          
            self.background_y += 1

            if self.background_y == 0 :
                self.background_y =  -125

    def draw_agua(self,delta_ms):
            self.time_elapsed += delta_ms
            if self.time_elapsed > self.time_interval:
                self.time_elapsed -= self.time_interval

            for x in range(self.rep_count_x):                    
                    self.screen.blit(self.image, (x * self.fotograma_ancho + self.background_x,  self.y))
            self.background_x += 2
            
            if self.background_x == 0 :
                self.background_x =  -126
                                
       
    

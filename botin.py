import pygame
from constantes import *
from auxiliar import Auxiliar


class Botin:

    def __init__(self,x,y,w,h,type,filas,columnas) -> None:

        self.image= Auxiliar.getSurfaceFromSpriteSheet("images\Fruits\\{0}.png".format(type),columnas,filas)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.frame = 0
        self.tiempo_transcurrido_animation = 0
        self.animation = self.image
        self.frame_rate_ms = 2
        self.image = pygame.transform.scale(self.animation[self.frame],(self.w,self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collition = pygame.Rect(self.rect.x + GROUND_RECT_W,self.rect.y + GROUND_RECT_H,self.rect.w/2,self.rect.h/3)

    def do_animation(self):   
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
            if DEBUG_PRINT:
                print("entre a cover fuuta")
        else: 
            self.frame = 0    

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition,2)
        

        self.image = self.animation[self.frame]
        self.image = pygame.transform.scale(self.image,(self.w,self.h))
        screen.blit(self.image,(self.rect.x,self.rect.y))

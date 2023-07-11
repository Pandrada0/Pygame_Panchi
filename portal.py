import pygame
from constantes import *
from auxiliar import Auxiliar

class Portal:

    def __init__(self,x,y,w,h,frame_rate_ms) -> None:
        
        self.image= Auxiliar.getSurfaceFromSpriteSheet(PORTAL,5,3)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.frame = 0
        self.tiempo_transcurrido_animation = 0
        self.animation = self.image
        self.frame_rate_ms = frame_rate_ms
        self.image = pygame.transform.scale(self.animation[self.frame],(self.w,self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w /3, self.rect.y + GROUND_RECT_H*2, self.rect.w /3, self.h - GROUND_RECT_H*3)

    def do_animation(self):   
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0    

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect,2)
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition,2)
        
        self.image = self.animation[self.frame]
        self.image = pygame.transform.scale(self.image,(self.w,self.h))
        screen.blit(self.image,(self.rect.x,self.rect.y ))

        
  

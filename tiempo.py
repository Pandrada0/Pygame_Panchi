import pygame
from constantes import *
from botin import Botin
import time
import os

class Tiempo:

    def __init__(self,x,y,w,minute,second) -> None:

        self.x = x
        self.y = y
        self.w = w
        self.minute = minute
        self.second = second
        self.time_elapsed = 0
        self.fuente = pygame.font.Font(None,  self.w) 
        self.texto_surface = self.texto = self.fuente.render("Time: {0}:{1}".format(self.minute,self.second), True, WHITE)
        self.sound_dead = pygame.mixer.Sound(SOUND_GAME_OVER) 
        self.is_sound = True
        self.is_dead = True
  
    def update(self,delta_ms):
        self.time_elapsed += delta_ms

        if self.time_elapsed > 1000:
            self.time_elapsed -= 1000

            if self.minute <= 0 and self.second <= 0 :
                self.minute = 0
                self.second = 0
                if self.is_sound:
                    self.is_sound = False
                    self.sound_dead.play()
                
            if self.second > 0 :
                self.second-= 1
            elif self.second == 0 and self.minute > 0:
                self.minute -= 1 
                self.second = 60 
      
            self.texto_surface = self.fuente.render("Time: {0}:{1}".format(self.minute,self.second),True,WHITE)
            
            if DEBUG_PRINT:
                 print("Time: {0}:{1}".format(self.minute,self.second))
   
    def draw(self,screen):

        screen.blit(self.texto_surface,(self.x , self.y))
            

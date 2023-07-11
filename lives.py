import pygame
from constantes import *
from auxiliar import *
from time import *


class Live:

    def __init__(self,x,y,w,h,live_x,live_y,live_w,live_h) -> None:

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = pygame.image.load("images\Fruits\\10.png")
        self.image = pygame.transform.scale(self.image,(live_w,live_h))
        self.rect_image = self.image.get_rect()
        self.rect_image.x = live_x
        self.rect_image.y = live_y
        self.rect_image.w = live_w
        self.rect_image.h = live_h
        self.live = 3 
        self.fuente = pygame.font.Font(None, self.w)
        self.texto_surface = self.fuente.render("Live:  {0}".format(self.live),True,WHITE)
        self.rect_ground_collition = pygame.Rect(self.rect_image.x + GROUND_RECT_W *4, self.rect_image.y + GROUND_RECT_H*4, self.rect_image.w/3, self.rect_image.h/3)
        self.seed = True

    def update (self,player):
        
        if self.rect_ground_collition.colliderect(player.rect) and self.seed:
            player.lives += 1
            volumen_actual = pygame.mixer.music.get_volume()
            if DEBUG_SOUND:
                pygame.mixer.music.get_volume(0.0)
            elif volumen_actual >= V_25:
                player.sound_ive.play()
            self.seed = False

        self.texto_surface = self.fuente.render("Live:  {0}".format(player.lives),True,WHITE)

    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen,RED,self.rect_image,2)
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition,2)
        screen.blit(self.texto_surface,(self.x,self.y))
        if self.seed:
            screen.blit(self.image,self.rect_image)
        
        

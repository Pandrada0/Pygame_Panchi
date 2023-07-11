import pygame
from constantes import *


class Score:
    def __init__(self,x,y,w,h) -> None:
        
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.score = 0
        self.fuente = pygame.font.Font(None, self.w)
        self.texto_surface = self.fuente.render("Score: {0}".format(self.score),True,WHITE)

        
    def swag(self,player,lista_botin):      

        for botin in lista_botin[::-1]:            
            if player.rect.colliderect(botin.rect_ground_collition):              
                self.score += 100
                self.texto_surface = self.fuente.render("Score: {0}".format(self.score),True,WHITE)
                lista_botin.remove(botin)
                volumen_actual = pygame.mixer.music.get_volume()
                if DEBUG_SOUND:
                    pygame.mixer.music.get_volume(0.0)
                elif volumen_actual >= V_25:
                    player.sound_score.play()
                if DEBUG:
                    print("recolecte fruta sumna 100p")

    def update(self,player,lista_botin):
        self.swag(player,lista_botin)

    def draw(self,screen):
        screen.blit(self.texto_surface,(self.x,self.y))
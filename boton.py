from player import *
from constantes import *
from auxiliar import Auxiliar


class Boton:

    def __init__(self,x,y,w,h,path) -> None:

        self.w = w
        self.h = h
        self.image = pygame.image.load(path)
        self.image_scale = pygame.transform.scale(self.image,(self.w,self.h))
        self.rect_image = self.image_scale.get_rect()
        self.rect_image.x = x
        self.rect_image.y = y
        self.is_clicked = False
        self.sound_click = pygame.mixer.Sound(SOUND_BOTON)

    def click(self):
        pos = pygame.mouse.get_pos()
        if self.rect_image.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.is_clicked = True
                volumen_actual = pygame.mixer.music.get_volume()
                if DEBUG_SOUND:
                    pygame.mixer.music.get_volume(0.0)
                elif volumen_actual > V_25:
                    self.sound_click.play()
                if DEBUG_PRINT:
                    print("click")
        if pygame.mouse.get_pressed()[0] == 0:
            self.is_clicked = False
        return self.is_clicked

    def draw(self,screen): 
        if DEBUG:
            pygame.draw.rect(screen,RED,self.rect_image,2)     
        screen.blit( self.image_scale,self.rect_image)
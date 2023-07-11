import pygame
from constantes import *



class Music:
    def __init__(self,path,volume=0.5) -> None:
        self.sound = pygame.mixer.music.load(path)
        self.sound_stop = None
        self.volumen = float(volume)

        self.sound_game_over = pygame.mixer.Sound(SOUND_GAME_OVER)
        self.sound_lvl_1 = pygame.mixer.Sound(SOUND_LVL_1)
        self.sound_lvl_2 = pygame.mixer.Sound(SOUND_LVL_2)
        self.sound_menu = pygame.mixer.Sound(SOUND_MENU)
        self.sound_game_over = pygame.mixer.Sound(SOUND_GAME_OVER)

    def volument(self,volumen):
        if volumen >= 0 and volumen <= 1:
            self.volumen = float(volumen)
            pygame.mixer.music.set_volume(volumen)
            if DEBUG_PRINT:
                print("Baje el volumen a ",volumen,"%")

    def play (self):
        pygame.mixer.music.play(-1)

    def stop(self):
         pygame.mixer.music.stop()

    def update(self,mute,volumen):
        self.volument(volumen)
        self.play_soun(mute)
    


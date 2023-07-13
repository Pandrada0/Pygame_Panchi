import pygame
from constantes import *

ANCHO_VENTANA = 1500
ALTO_VENTANA = 800
FPS = 240
FPS_DOBLE = FPS*2
FPS_MITAD = FPS/2

PATH_IMAGE = "/CLASE_19_inicio_juego/images/"


DIRECTION_L = 0
DIRECTION_R = 1
ALTO_PLAYER = 60
ANCHO_PLAYER = 60

GROUND_LEVEL = 550
DEBUG = False
DEBUG_PRINT = False
DEBUG_SOUND = False


# COLOR CONSTANTS
RED = (255,0,0)
GREEN = (0,255,0)
SKY_BLUE = (0,191,255)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

# rect player
GROUND_RECT_H = 8
GROUND_RECT_W = 8


# Menu
FONDO_MENU = "images\mi_menu\\2.png"

# fondo agua
FONDO_AGUA = "images\lvl_1\Tiles\\17.png"

# flecha inicio
FLECHA_INICIO = "images\lvl_1\Tiles\\20.png"
# lvl 1
IMAGE_TILTES_1 = "images\lvl_1\Tiles"
FONDO_LVL_1 = "images\lvl_1\\fondo\Blue.png"

# lvl 2
IMAGE_TILTES_2 = "images\lvl_2\Tiles_2"
FONDO_LVL_2 = "images\lvl_2\\fondo\Purple.png"
FONDO_PINCHES_LVL_2 = "images\lvl_2\\fondo\Spike.png"

# lvl 3

IMAGE_TILTES_3 = "images\lvl_3\Tiles_3"
FONDO_LVL_3 = "images\lvl_3\\fondo\Pink.png"


# Fondo info
FONDO_INFO = "images\info\info.png"

# Portal
PORTAL = "images\portal\\1.png"

# Frutas
FRUTAS = "images\Fruits\\"

#SETTING
FONDO_SETTING = "images\setting\\fondo.png"
TITULO_SETTING = "images\setting\\titulo.png"
TABLA_SETTING = "images\setting\\table.png"
PREW_SETTING = "images\setting\prew.png"

# Game Over
GAME_OVER = "images\game_over\header.png"


#music
SOUND_MENU = "sound\menu.mp3"
SOUND_BOTON = "sound\\boton.mp3"
SOUND_LVL_1 = "sound\lvl1.mp3"
SOUND_LVL_2 = "sound\lvl2.mp3"
SOUND_FRUTAS = "sound\\frutas.mp3"
SOUND_GAME_OVER = "sound\game_over.mp3"
SOUND_VIDA = "sound\\vida.mp3"
SOUND_PLAYER_MUERTE = "sound\muerte.mp3"
SOUND_PLAYER_SALTO = "sound\salto.mp3"
SOUND_LVL_3 = SOUND_LVL_2
SOUND_WIN = "sound\win.mp3"
# Volumen
V_0 = 0.0
V_25 = 0.25
V_50 = 0.50
V_75 = 0.75
V_100 = 1




# Import a library of functions called 'pygame'
import pygame
from main_functions import *

# Initialize the game engine
pygame.init()

#call main routine
ancho = int(input("ancho de la ventana: "))
alto = int(input("alto de la ventana: "))
size = (ancho, alto)
main2(size)
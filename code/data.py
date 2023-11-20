import pygame
from pygame import Surface as Surf

isInputAllowed = True
def getInput(input:int):
    if pygame.key.get_focused() and isInputAllowed:
        return pygame.key.get_pressed()[input]
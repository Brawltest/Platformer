import pygame
from pygame import Surface as Surf

class Window(pygame.Surface):
    screen_widht : int
    screen_height : int
    screen_size : pygame.Vector2
    screen_surf : Surf
    def __init__(self, size: pygame.Vector2,) -> None:
        self.screen

isInputAllowed = True
def getInput(input:int):
    if pygame.key.get_focused() and isInputAllowed:
        return pygame.key.get_pressed()[input]
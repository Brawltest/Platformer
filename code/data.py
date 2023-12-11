import pygame
from pygame import Surface as Surf, Surface
from code.PathToSprite import Surface, pygame
from sprites import AnimatedSprite
from typing import overload
import ctypes

Coordinate = list[int,int]
Collision_List : list
gravity = 0.1

isInputAllowed = True
def getInput(input:int):
    if pygame.key.get_focused() and isInputAllowed:
        return pygame.key.get_pressed()[input]

class KASprite(AnimatedSprite):
    """### Kinematic Animated Sprite
    Used to have a animated Sprite w/ collision"""
    velocity : pygame.Vector2
    acceleration : pygame.Vector2
    weight : float
    position : Coordinate
    col_rect : pygame.Rect
    mask : pygame.mask.Mask
    use_mask : bool = False
    act_surf : pygame.Surface
    
    def __init__(self, position: Coordinate, images: list[Surface],rect : pygame.Rect):
        super().__init__(position, images)
        self.col_rect = rect
        
    @overload
    def __init__(self, position: Coordinate, images: list[Surface], use_mask:bool=True):
        """Use mask (image) as collition (not recommended for aniamted)
        put `use_mask=True` to use that feature"""
        super().__init__(position,images)
        self.use_mask = True
        self.mask = pygame.mask.from_surface(self.image) #Use First Image as mask
    
    def colition_point(self,point : Coordinate) -> bool:
        if self.use_mask:
            self.mask = pygame.mask.from_surface(self.image)
            point_mask = pygame.mask.Mask((1,1),True)
            self.image.
    def get_mask


"""
pygame.sprite.spritecollide(src:Sprite,dst:Group,kill:bool,Mask)
pygame.mask.from_surface().to_surface() -> Cool
"""
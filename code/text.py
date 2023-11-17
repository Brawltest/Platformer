from typing import Optional
import pygame

isNone = lambda x: (x == None)
pygame.font.init()

class Text():
    pos = pygame.Vector2(0,0)
    fontname = pygame.font.get_default_font()
    text = "None"
    size = 16
    font = pygame.font.Font(fontname,size)

    def __init__(self,text:str, size:int, fontname:str, pos: pygame.Vector2 | None = None) -> None:
        if isNone(pos): pos = pygame.Vector2(0,0)
        if isNone(text): self.text = text
        if isNone(size): self.size = size
        if isNone(fontname): self.fontname = pygame.font

    def changeSize(self,size:int):
        if isNone(size): pass
        else: pygame.font.Font(self.fontname,size); self.size = size

    def update(self,text,surf:pygame.Surface):
        self.surf = pygame.Surface(self.font.size(text),pygame.SRCALPHA).convert_alpha()
        self.surf.blit(self.font.render(text,True,(255,255,255,255),(0,0,0,0)).convert_alpha(),self.pos)
        return self.surf
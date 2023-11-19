from typing import Optional
import pygame
from tkinter.messagebox import showerror

isNone = lambda x: (x == None)
pygame.font.init()

class Text():
    """
    Ceci est un classe qui permet de créer un texte avec pygame.

    ### Arguments / Paramètres
    - `size` : La taille de police
    - `fontname` : le nom de la police
    - `text` : le texte par défaut
    - `bold` : si le texte est en gras
    - `italic` : si le texte est en italique
    """


    pos = pygame.Vector2(0,0)
    fontname = pygame.font.get_default_font()
    text = "None"
    size = 16
    color : pygame.Color
    font : pygame.font.Font
    bold : bool = False
    italic : bold = False
    antialias : bold = True

    def __init__(self, size:int = 16,
                 fontname:str = "None",
                 text:str = "None",
                 color : pygame.Color = (255,255,255,255),
                 backgroundcolor : pygame.Color = (0,0,0,0),
                 antialias = True,
                 bold = False,
                 italic = False) -> None:
        self.text = text
        self.size = size
        self.fontname = fontname
        self.antialias = antialias
        self.color = color
        self.bgcolor = backgroundcolor
        if isNone(fontname): self.fontname = pygame.font.get_default_font()
        if not (fontname in pygame.font.get_fonts()):
            showerror("Erreur de Police",f"La police \"{fontname}\" n'existe pas ! ")
            self.fontname = pygame.font.get_default_font()
        self.font = pygame.font.SysFont(self.fontname,self.size,bold,italic)
        
    def changeSize(self,size:int):
        if isNone(size): self.size = 32
        else: self.size = size
        self.font = pygame.font.SysFont(self.fontname,self.size,self.bold,self.italic)

    def update(self,text:str | None = None):
        if text != None: self.text = text
        self.surf = pygame.Surface(self.font.size(self.text),pygame.SRCALPHA).convert_alpha()
        self.surf.blit(self.font.render(self.text,self.antialias,self.color,self.bgcolor).convert_alpha(),self.pos,special_flags=pygame.BLEND_RGBA_ADD)
        return self.surf
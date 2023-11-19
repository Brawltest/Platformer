import pygame, settings, data, sprites, text

pygame.init()

class Game(pygame.surface.Surface):

    screen: pygame.Surface
    size: tuple[int,int]
    flags: int
    keys : list[int]
    icon : pygame.Surface
    clock : pygame.time.Clock

    def __init__(self,size: tuple[int,int] | None = None,flags:int | None = None):
        if size == None: self.size = settings.Screen.Size
        else : self.size = size
        if flags == None or flags == 0: self.flags = settings.Screen.Flags
        else : self.flags = flags

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.size,self.flags)
        self.icon = pygame.image.load(settings.Screen.Icon)
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption(settings.Screen.Caption)

        self.spr_mario = sprites.load_images_wscreen("./gfx/Animations/Idle/")
        self.ani_mario = sprites.AnimatedSprite((0,0),self.spr_mario)
        self.pos = (settings.Screen.Widht/2 - self.ani_mario.image.get_width()*2/2,
                    settings.Screen.Height/2 - self.ani_mario.image.get_height()*2/2)
        print(pygame.font.get_fonts())
        
        #Test de texte en dessous avec divers example
        self.txt_debug = text.Text(32,"arial") #Texte normal en Arial (aucune couleur)
        self.txt_debug2 = text.Text(20,"comicsansms") #Texte en Comic Sans (aucune couleur)
        self.txt_frame = text.Text(20,"arial","Frame",(0,150,0,255),"black",False,True,True) #Text en vert (150green) avec fond "black" en Gras et Italic mais pas en alias
        self.txt_framerate = text.Text(24,"timesnewroman","Framerate",(255,255,255,150),(0,150,0,255)) #Texte qui affiche le nombre de FPS avec un fond "vert" (150green) et un texte un peut transparent (150/255 % transparent)
        self.txt_mario = text.Text(24,"calibri","It's a me MARIO",(0,0,255,10),(0,0,255,10),True,True,False) #Test de Transparent

    def step(self):
        self.ani_mario.update_frame_dependent()
        self.screen.blit(self.ani_mario.scale(2),self.pos)
        self.screen.blit(self.txt_debug.update("Voici un texte blanc"),(10,10))
        self.screen.blit(self.txt_debug2.update("Voici un deuxième texte"),(10,50))
        self.screen.blit(self.txt_frame.update("Frame : {0}/{1}".format(self.ani_mario.index,len(self.ani_mario.images))),(10,240))
        self.screen.blit(self.txt_framerate.update("FPS : {0}".format(int(self.clock.get_fps()))),(10,270))
        self.screen.blit(self.txt_mario.update("It's a me mario"),(100,120))
        self.clock.tick(settings.Screen.Framerate)
    def _CheckEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                try:
                    print(pygame.key.name(event.key))
                except:
                    print("Fail :'(")
            
    def _UpdateScreen(self):
        pygame.display.flip()
    def loop(self):
        while True:
            self._CheckEvents()
            self.screen.fill((0,0,0))
            self.step()
            self._UpdateScreen()
            

if __name__ == '__main__':
    game = Game()
    game.loop()
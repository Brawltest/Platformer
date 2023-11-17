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

        self.spr_mario = sprites.load_images("./gfx/Animations/Idle/")
        self.ani_mario = sprites.AnimatedSprite((0,0),self.spr_mario)
        self.pos = (settings.Screen.Widht/2 - self.ani_mario.image.get_width()/2,
                    settings.Screen.Height/2 - self.ani_mario.image.get_height()/2)

    def step(self):
        self.ani_mario.update_frame_dependent()
        self.screen.blit(self.ani_mario.image,self.pos)
        self.clock.tick(settings.Screen.Framerate)
    def _CheckEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(1)
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
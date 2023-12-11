import pygame, os, sys
from pygame.sprite import AbstractGroup, Sprite, Group
from pygame import Surface
from tkinter.filedialog import *
import tkinter.messagebox as msgb
from PathToSprite import *
import time, re
import tkinter as tk
import tkinter.ttk as tkk

#MovingSprite = pygame.sprite.Group()
def sortNumbInList(unsortedlist:list[str]):
    try:
        sorted_list = sorted(unsortedlist, key=lambda x: int(re.findall(r'\d+', x)[0]))
    except IndexError as ie:
        if len(unsortedlist) > 1:
            msgb.showerror(str(type(ie)),
            f"""
            Unsorted List :
            {unsortedlist}

            Does not cointain number(s) in every strings !""")
        else:
            msgb.showerror(str(type(ie)),
            f"""
            Unsorted List :
            {unsortedlist}

            Does not cointain number(s) in string !""")
        exit(ie)
    print(sorted_list)
    return sorted_list

def load_images(path) -> list[Surface]:
    images = []
    print(os.listdir(path))
    pathimages = sortNumbInList(os.listdir(path))
    for pathimg in pathimages:
        print(path + pathimg)
        images.append(pygame.image.load(path + pathimg, ".png"))
    return images

def load_images_wscreen(path) -> list[Surface]:
    images = []
    amount = len(os.listdir(path))
    app = tk.Tk(screenName="Loading")
    lab = tk.Label(app,text="Loading")
    lab.pack(padx=10,pady=10)
    load = tkk.Progressbar(app,mode='determinate',length=300,maximum=len(os.listdir(path)),orient='horizontal')
    load.pack(padx=10,pady=10)
    
    print(os.listdir(path))
    pathimages = sortNumbInList(os.listdir(path))
    for index,pathimg in enumerate(pathimages):

        load.config(value=index,maximum=len(os.listdir(path)))
        lab.config(text=f'Loading : {index+1}/{amount}')
        app.update_idletasks()
        app.update()
        time.sleep(0.04)
        if index == 20:
            time.sleep(1)
        print(path + pathimg)
        images.append(pygame.image.load(path + pathimg, ".png"))
    time.sleep(0.5)
    app.destroy()
    return images
    
    
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, position: pygame.Vector2, images: list[Surface]):
        """
        Animated sprite object.

        ### Args:
        `position`: x, y coordinate on the screen to place the AnimatedSprite.
        `images`: Images to use in the animation.
        """
        super(AnimatedSprite, self).__init__()
        size = (32, 32)  # This should match the size of the images.

        self.rect = pygame.Rect(position, size)
        self.images = images
        self.images_right = images
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]  # Flipping every image.
        self.index = 0
        self.image = images[self.index]  # 'image' is the current image of the animation.

        self.animation_time = 0.1
        self.current_time = 0

        self.animation_frames = 6
        self.current_frame = 0

    def update_time_dependent(self, dt : int):
        """
        Updates the image of Sprite approximately every 0.1 second.
        Args:
            dt: Time elapsed between each frame.
        """
        if self.velocity.x > 0:  # Use the right images if sprite is moving right.
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
        self.rect.move_ip(*self.velocity)

    def update_frame_dependent(self):
        """
        Updates the image of Sprite every 6 frame (approximately every 0.1 second if frame rate is 60).
        Updates the image of Sprite every frame (depend on Clock tick).
        """
        if self.velocity.x > 0:  # Use the right images if sprite is moving right.
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left
        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
        self.rect.move_ip(*self.velocity)

    def resize(self,size:pygame.Vector2):
        return pygame.transform.scale(self.image,[*size])
    
    def scale(self,scale:int):
        return pygame.transform.scale(self.image,[self.image.get_width()*scale,self.image.get_height()*scale])


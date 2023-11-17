import pygame, os
from pygame.sprite import Sprite
from pygame.surface import Surface
from tkinter.filedialog import *
from tkinter.dialog import Dialog, DIALOG_ICON

def ImgStr_To_Sprite(path:str):
    try:
        img = pygame.image.load(path)
    except Exception as e:
        d = Dialog(None, {'title': 'Failed Loading',
                      'text':
                      f'File "{path}" have failed to load'
                      ' Since this file need to be loaded,'
                      ' The game cannot go any futher.'
                      ' Exiting the application ?'
                      ' '
                      f' Error : {e}',
                      'bitmap': DIALOG_ICON,
                      'default': 2,
                      'strings': ('Locate Image',
                                  'Save Error',
                                  'Exit Game')})
        match (d.num):
            case 0:
                f = askopenfilename('r',filetypes=(["PNG","*.png"],["JPEG1",'*.jpeg'],["JPEG","*.jpg"]))
                try:
                    img = pygame.image.load(filename=f)
                except:
                    exit("FUCK")
                finally:
                    pass
            case 1:
                f = asksaveasfile(mode='w')
                if f is None:
                    f.write(str(e))
                    exit("Saved")
                else:
                    exit("Not Saved")
            case 2:
                exit("Exited")
    
    return img


def AllImageFromFolder(path) -> list[Surface]:
    images = []
    for pathimg in os.listdir(path):
        images.append(pygame.image.load(pathimg))
    return images
import os
import glob
import pygame

def dprint(arg):
    print arg

def get_path(fname):
   return os.path.join(__path__[0],fname)

def load_sound(rname):
   return pygame.mixer.Sound(get_path(rname))

def load_sounds(pattern):
   return [pygame.mixer.Sound(x) for x in sorted(glob.glob(get_path(pattern)))]

def load_image(rname):
   return pygame.image.load(get_path(rname))

def load_images(pattern):
   return [pygame.image.load(x) for x in sorted(glob.glob(get_path(pattern)))]


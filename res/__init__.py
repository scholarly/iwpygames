import os
import glob
import pygame

def dprint(arg):
    print arg

def get_path(fname):
   return os.path.join(__path__[0],fname)

def load_sound(rname):
   return pygame.mixer.Sound(get_path(fname))

def load_sounds(pattern):
   #dprint(pattern)
   return [pygame.mixer.Sound(x) for x in sorted(glob.glob(get_path(pattern)))]

   

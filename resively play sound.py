import time
import os
import glob 
import pygame 

path = r"/usr/share/scratch/"

directory = "/usr/share/scratch"
pathname = directory + "/**/*.mp3"
files = glob.iglob(pathname, recursive=True)
print(files)
print(pathname)
for filename in glob.iglob('/usr/share/scratch/**/*.mp3', recursive=True):
    print(filename)
    pygame.mixer.init()
#   todo ensure mp3
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    time.sleep(1)
print("Audio Files Exhasted")
    
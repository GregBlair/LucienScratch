import time
import os
import pygame 




# while True:
#     import pygame
#     pygame.mixer.init()
#     pygame.mixer.music.load("/usr/share/scratch/Media/Sounds/Music Loops/Triumph.mp3")
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy() == True:
#         continue
#     time.sleep(3)
# 

 
# specify your path of directory
path = r"/usr/share/scratch/Media/Sounds/Music Loops"
 
# call listdir() method
# path is a directory of which you want to list
directories = os.listdir( path )
 
# This would print all the files and directories
# for file in directories:
#    print(file)
# todo walk direstories
for files in directories:
    
    print(files)
    if os.path.isfile(os.path.join(path, files)):
        print(os.path.join(path, files))
        
        pygame.mixer.init()
#         todo ensure mp3
        pygame.mixer.music.load(os.path.join(path, files))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        time.sleep(1)
print('')
print('finished')

print('wewiybeuityenityeuit34y57834y5347856754vn9 35y683476y738y3itvynukvey5783t78v53y5iu3y5i3vy583')
        
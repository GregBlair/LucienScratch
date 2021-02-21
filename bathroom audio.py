

while True:
if isDoorOpen():
    print('door is open')
    
     pygame.mixer.init()
    pygame.mixer.music.load("/usr/share/scratch/Media/Sounds/Music Loops/Triumph.mp3")
     pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
             continue
    time.sleep(SLEEP_TIME_SEC)
    GPIO.output(GPIO_OUTPUT_PIN, GPIO.HIGH)

else:
    print('door is closed')
        
    GPIO.output(GPIO_OUTPUT_PIN, GPIO.LOW)
    
time.sleep(SLEEP_TIME_SEC)
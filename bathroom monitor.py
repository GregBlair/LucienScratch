    import time
    import random
    import RPi.GPIO as GPIO
    import pygame
    import constants as CS 

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(CS.GPIO_OUTPUT_PIN, GPIO.OUT)


    def isDoorOpen():
        number=random.randint(0,12)
        print(number)
        return number<6

    while True:
        if isDoorOpen():
            print('door is open')
            
            
            time.sleep(CS.SLEEP_TIME_SEC)
            GPIO.output(CS.GPIO_OUTPUT_PIN, GPIO.HIGH)

        else:
            print('door is closed')
                
            GPIO.output(CS.GPIO_OUTPUT_PIN, GPIO.LOW)
            
            time.sleep(CS.SLEEP_TIME_SEC)       
        

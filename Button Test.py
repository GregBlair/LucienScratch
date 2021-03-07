import time
# import random
import RPi.GPIO as GPIO
# import pygame

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
# GPIO.setmode( GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True: 
    print("Testing now!")
    if GPIO.input(12) == GPIO.HIGH:
        print("Button was pushed!")
        GPIO.output(16, GPIO.HIGH)
        print("Sleeping for 3!")
        time.sleep(3)
        GPIO.output(16, GPIO.LOW)
    
        


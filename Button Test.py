import time
# import random
import RPi.GPIO as GPIO
# import pygame

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
# GPIO.setmode( GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True: 
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pushed!")
        GPIO.output(18, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(18, GPIO.LOW)
    
        


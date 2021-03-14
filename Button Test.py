import time
# import random
import RPi.GPIO as GPIO
# import pygame
import constants as CS 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
# GPIO.setmode( GPIO.BCM)
GPIO.setup(CS.GPIO_OUTPUT_PIN, GPIO.OUT)
GPIO.setup(CS.GPIO_INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True: 
    print("Testing now!")
    if GPIO.input(CS.GPIO_INPUT_PIN) == GPIO.HIGH:
        print("Button was pushed!")
        GPIO.output(CS.GPIO_OUTPUT_PIN, GPIO.HIGH)
        print("Sleeping for 3!")
        time.sleep(3)
        GPIO.output(CS.GPIO_OUTPUT_PIN, GPIO.LOW)
    
        


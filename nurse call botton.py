import time
import random
import RPi.GPIO as GPIO
import pygame
import constants as CS

GPIO.setmode(GPIO.BCM)
GPIO.setup(CS.GPIO_PATIENT_OUTPUT_PIN, GPIO.OUT)
GPIO.setup(CS.GPIO_NURSE_OUTPUT_PIN, GPIO.OUT)
GPIO.setup(CS.GPIO_PATIENT_INPUT_PIN, GPIO.IN)
GPIO.setup(CS.GPIO_NURSE_INPUT_PIN, GPIO.IN)

STATE=CS.WAITING

def isPatietButtonPushed():
        number=random.randint(1,10)
        print(number)
        return number<9

while True:
            if isPatietButtonPushed():
            STATE=CS.WAITING
            print('patient button has been pushed ')
            GPIO.output(CS.GPIO_PATIENT_OUTPUT_PIN, GPIO.HIGH)
            GPIO.output(CS.GPIO_NURSE_OUTPUT_PIN, GPIO.HIGH)
                    

        else:
            print('patient button has not been pushed')
            GPIO.output(CS.GPIO_NURSE_OUTPUT_PIN, GPIO.LOW)
            GPIO.output(CS.GPIO_PATIENT_OUTPUT_PIN, GPIO.LOW)
            STATE=CS.WAITING
        
        def PLAY_AMARM_SOUND
            if STATE=CS.WAITING
            play
            
        time.sleep=(CS.LIGHT_DELAY)

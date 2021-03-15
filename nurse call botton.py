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


def isPatietButtonPushed():
        number=random.randint(0,12)
        print(number)
        return number<6

while True:
        if isPatietButtonPushed():
            print('patient button has been pushed ')
            GPIO.output(CS.GPIO_PATIENT_OUTPUT_PIN, GPIO.HIGH)
            GPIO.output(CS.GPIO_NURSE_OUTPUT_PIN, GPIO.HIGH)
                        
            time.sleep(CS.LIGHT_DELAY)

        else:
            print('patient button has not been pushed')
            GPIO.output(CS.GPIO_NURSE_OUTPUT_PIN, GPIO.LOW)
            GPIO.output(CS.GPIO_PATIENT_OUTPUT_PIN, GPIO.LOW)
            
        time.sleep(CS.LIGHT_DELAY)       

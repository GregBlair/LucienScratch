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


def playAlarmSound():
    pygame.mixer.init()
    pygame.mixer.music.load("/usr/share/scratch/Media/Sounds/Effects/WaterRunning.mp3")
    pygame.mixer.music.play()
    print("Alarm is sounding!")
    while pygame.mixer.music.get_busy() == True:
        continue
            
def isPatietButtonPushed():
        number=random.randint(1,10)
        print(number)
        return number<2

def isNurseButtonPushed():
        number=random.randint(1,10)
        print(number)
        return number<4
 
STATE=CS.IDLE

while True:
    if isPatietButtonPushed():
        STATE=CS.WAITING
        print('patient button has been pushed ')
        GPIO.output(CS.GPIO_PATIENT_OUTPUT_PIN, GPIO.HIGH)
        GPIO.output(CS.GPIO_NURSE_OUTPUT_PIN, GPIO.HIGH)
                    

    else:
        if isNurseButtonPushed():
            print('nurse button has been pushed')
            GPIO.output(CS.GPIO_NURSE_OUTPUT_PIN, GPIO.LOW)
            GPIO.output(CS.GPIO_PATIENT_OUTPUT_PIN, GPIO.LOW)
            STATE=CS.IDLE
        
    if STATE==CS.WAITING:
        playAlarmSound()
    
    time.sleep(CS.LIGHT_DELAY)

import time
import random
import RPi.GPIO as GPIO
import pygame
import constants as CS

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(CS.GPIO_PATIENT_INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(CS.GPIO_NURSE_INPUT_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#GPIO.setmode(GPIO.BCM)
GPIO.setup(CS.GPIO_PATIENT_OUTPUT_PIN, GPIO.OUT)
GPIO.setup(CS.GPIO_NURSE_OUTPUT_PIN, GPIO.OUT)
# GPIO.setup(CS.GPIO_PATIENT_INPUT_PIN, GPIO.IN)
# GPIO.setup(CS.GPIO_NURSE_INPUT_PIN, GPIO.IN)


patientButtonPushed = False
def patient_button_callback(channel):
    print("Patient button callback!")
    global patientButtonPushed = True
    
def playAlarmSound():
    GPIO.output(CS.GPIO_NURSE_OUTPUT_PIN, GPIO.HIGH)
    pygame.mixer.init()
    pygame.mixer.music.load(CS.ALARM_NOISE)
    pygame.mixer.music.play()
    print("Alarm is sounding!")
    while pygame.mixer.music.get_busy() == True:
        continue
    GPIO.output(CS.GPIO_NURSE_OUTPUT_PIN, GPIO.LOW)
            
def isPatietButtonPushed():
    return patientButtonPushed

def isNurseButtonPushed():
    return GPIO.input(CS.GPIO_NURSE_INPUT_PIN) == GPIO.HIGH

GPIO.add_event_detect(CS.GPIO_PATIENT_INPUT_PIN,
                      GPIO.RISING,
                      callback=patient_button_callback) # Setup event on patient button pin rising edge

STATE=CS.IDLE

while True:
    if STATE==CS.IDLE:
        if isPatietButtonPushed():
            STATE=CS.WAITING
            print('patient button has been pushed ')
            GPIO.output(CS.GPIO_PATIENT_OUTPUT_PIN, GPIO.HIGH)
      
                    

    elif STATE==CS.WAITING:
        if isNurseButtonPushed():
            print('nurse button has been pushed')
            
            GPIO.output(CS.GPIO_PATIENT_OUTPUT_PIN, GPIO.LOW)
            STATE=CS.IDLE
    
        else:
            playAlarmSound()
            
    time.sleep(CS.LIGHT_DELAY)

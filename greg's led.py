import time
import random
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

def isDoorOpen():
    number=random.randint(0,12)
    print(number)
    return number<6


while True:
    if isDoorOpen():
        print('door is open')
        GPIO.output(18, GPIO.HIGH)
    else:
        print('door is closed')
        GPIO.output(18, GPIO.LOW)
    time.sleep(3)
        
    

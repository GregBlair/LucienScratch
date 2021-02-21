import RPi.GPIO as GPIO
import time
SLEEP_TIME_SEC = 10
GPIO_OUTPUT_PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(GPIO_OUTPUT_PIN,GPIO.OUT)
print("LED on")
GPIO.output(GPIO_OUTPUT_PIN,GPIO.HIGH)
time.sleep(SLEEP_TIME_SEC)
print("LED off")
GPIO.output(GPIO_OUTPUT_PIN,GPIO.LOW)
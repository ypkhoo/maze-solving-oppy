import RPi.GPIO as GPIO
import time

def init(): 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(15,GPIO.OUT)

init()
GPIO.cleanup()

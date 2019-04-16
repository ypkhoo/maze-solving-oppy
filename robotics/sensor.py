import RPi.GPIO as GPIO
import time

TRIG = 12
ECHO = 16

def distance(): 
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
    #GPIO.output(TRIG, False)
    #print ("Waiting For Sensor To Settle")
    #time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)

    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0: 
        noSignal = time.time() 
    while GPIO.input(ECHO) == 1:
        signal = time.time()

    timeDiff = signal - noSignal 

    distance = timeDiff * 17150
    
    GPIO.cleanup()
    return distance


import RPi.GPIO as GPIO 
import time 
from sensor import distance 

def init(): 

    """
    PIN7 = left forward
    PIN11 = left reverse
    PIN13 = right reverse
    PIN15 = right forward
    """
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)

def forward(timeFrame): 
    init()
    GPIO.output(7, True)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, True)
    time.sleep(timeFrame)
    GPIO.cleanup()

def reverse(timeFrame): 
    init() 
    GPIO.output(7, False)
    GPIO.output(11, True)
    GPIO.output(13, True)
    GPIO.output(15, False)
    time.sleep(timeFrame)
    GPIO.cleanup()

def turn_left(timeFrame): 
    init() 
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, True)
    time.sleep(timeFrame)
    GPIO.cleanup() 

def turn_right(timeFrame): 
    init() 
    GPIO.output(7, True)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    time.sleep(timeFrame)
    GPIO.cleanup() 

def pivot_left(timeFrame): 
    init() 
    GPIO.output(7, False)
    GPIO.output(11, True)
    GPIO.output(13, False)
    GPIO.output(15, True)
    time.sleep(timeFrame)
    GPIO.cleanup() 

def pivot_right(timeFrame): 
    init() 
    GPIO.output(7, True)
    GPIO.output(11, False)
    GPIO.output(13, True)
    GPIO.output(15, False)
    time.sleep(timeFrame)
    GPIO.cleanup()

def checkAllDist(): 
    frontDist = distCheck()
    pivot_left(0.3)
    leftDist = distCheck()
    pivot_right(0.6)
    rightDist = distCheck()
    pivot_left(0.3)
    distList = [rightDist, leftDist, frontDist]
    return distList

def testMvmt(timeFrame): 
    init()
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, True)
    time.sleep(timeFrame)
    GPIO.cleanup()
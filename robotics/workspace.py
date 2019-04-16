import RPi.GPIO as GPIO 
import time 

TRIG = 12
ECHO = 16

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
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

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

def testMvmt(timeFrame): 
    init()
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, True)
    time.sleep(timeFrame)
    GPIO.cleanup()

def distance(): 
    init()
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

def speed(): 
    dist1 = distance()
    forward(1)
    dist2 = distance()
    speed = dist1-dist2/1
    return speed 

def driveTime(distance):
    distance -= 3
    drivingTime = distance /37.38
    return drivingTime

def checkAllDist(): 
    distList = []
    time.sleep(0.5)
    frontDist = distance() 
    pivot_left(0.68)
    time.sleep(0.5)
    leftDist = distance()
    pivot_right(1.34)
    time.sleep(0.5)
    rightDist = distance()
    pivot_left(0.68)
    distList = [leftDist, frontDist, rightDist]
    return distList

def driveStraight(): 
    frontDist = distance()
    drivingTime = driveTime(frontDist)
    forward(drivingTime)

def main():
    return 0

if __name__ =="__main__":
    main()

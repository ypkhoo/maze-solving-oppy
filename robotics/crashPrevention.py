import sensor
import movement
import RPi.GPIO as GPIO

def driveToObs(): 
    tmpDist = distCheck()
    while tmpDist >= 20: 
        print("I am in while")
        movement.forward(0.2)
        tmpDist = distCheck()
    return tmpDist

def checkAllDist(): 
    frontDist = distCheck()
    pivot_left(0.3)
    leftDist = distCheck()
    pivot_right(0.6)
    rightDist = distCheck()
    pivot_left(0.3)
    distList = [rightDist, leftDist, frontDist]
    return distList

def distCheck():
    tmpDist = sensor.distance() 
    if tmpDist <= 20: 
        print("Terminated by force")
    return tmpDist

def lookToLeft(): 
    tmpDist = sensor.distance() 
    print("Distance: "+ str(tmpDist) + " Look To Left Now")
    if tmpDist <= 20: 
        movement.pivot_left(0.4)
    return tmpDist

def lookToRight(): 
    tmpDist = sensor.distance() 
    print("Distance: " + str(tmpDist) + " Look To Right Now")
    if tmpDist <= 20: 
        movement.pivot_right(0.7)
    return tmpDist

#print(sensor.distance())
stopDist = driveToObs()
print("Stopped, distance = " + str(stopDist))
if distCheck <= 20: 
    leftDist = lookToLeft() 
    print("Look to left, distance = " + str(leftDist))
    rightDist = lookToRight() 
    print("Look to right, distance = "+ str(rightDist))
#lookToLeft()
#movement.reverse(1)

import movement as mvmt
#from sensor import *

def main():
    workingList = []
    workingList = mvmt.checkAllDist()

    # detecting start, drives straight, until left&right > threshold
    while workingList[-1] >= 50 and workingList[0] <= 10\
          and workingList[1] <= 10:
        mvmt.forward(3)
        workingList = mvmt.checkAllDist() 



if __name__ == "__main__":
    main()

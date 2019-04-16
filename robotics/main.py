import movement as mvmt
import sensor as ssr
import workspace as ws

def main():
    distList = [0,0,0]
    average = sum(distList)/len(distList)
    ws.driveStraight() 
    distList = ws.checkAllDist()
    print(distList)
    average = sum(distList)/len(distList)
    print(average)
    while average < 50: 
        print(distList)
        average = sum(distList)/len(distList)
        print(average)
        if average < 10: 
            mvmt.pivot_left(1.34)
        elif distList[0] == max(distList): 
            mvmt.pivot_left(0.68)
            ws.driveStraight()
        elif distList[1] == max(distList): 
            print("error")
        elif distList[2] == max(distList): 
            mvmt.pivot_right(0.68)
            ws.driveStraight()
        else: 
            mvmt.pivot_left(1.25)
    #mvmt.reverse(0.8)
    #mvmt.pivot_left(2.35)

if __name__ == "__main__":
    main()

#Lab Two
#Logan Kilpatrick
#09/27/2017

from ezgraphics import GraphicsWindow

#CIS 41A - Lab 2: arithmetic, IO, graphics
#In one Python file called lab2.py, write code for 2 problems from the textbook.
#1. (P2.17)
#Write a program that reads in two times in military format (0900, 1730) and prints the number of hours and minutes between the...
#two times. You can assume the input time is always a valid, 4-digit number.
#Example output (user input in blue):
    #Please enter the start time: 0900
    #Please enter the end time: 1730
    #8 hours, 30 minutes
#2. (P2.30)
#Write a program that displays the Olympic rings. Color the rings in the Olympic colors.
#In addition to the graphics methods shown in the class notes, use the Source Assistant...
#feature of the IDE to help you set the pen size so it's thicker than the default size.
#add in texts that "The Olympics"




#Start of actual code 

def convertInputToData():
    
    userInputStart = input("Please enter the start time")
    userInputEnd = input("Please enter the end time")    
    
    hours1 = userInputStart[0]
    hours1 += userInputStart[1]    
    
    hours2 = userInputEnd[0]
    hours2 += userInputEnd[1]
    
    
    minutes1 = userInputStart[2]
    minutes1 += userInputStart[3]    
    
    minutes2 = userInputEnd[2]
    minutes2 += userInputEnd[3]
    
    
    print((int(hours2)-int(hours1)), " hours, " , (int(minutes2)-int(minutes1)) , "minutes")#prints the full requested solution

    
    
#The below code runs part One of Lab Two  


convertInputToData()#calls part one 

#PartTwo of Lab two 
def olympicRings():
    win = GraphicsWindow(640, 480)
    canvas = win.canvas()
    z = 20
    w = 15
    canvas.setLineWidth(10)#changes the size of the line! 
    canvas.setOutline("blue")
    canvas.drawOval(100,100,100,100)
    
    canvas.setOutline("black")
    canvas.drawOval(175,100,100,100)
    
    canvas.setOutline("red")
    canvas.drawOval(250,100,100,100)   
    
    canvas.setOutline("yellow")
    canvas.drawOval(135,150+w,100,100)    
    
    canvas.setOutline("green")
    canvas.drawOval(215,150+w,100,100)        
    
    canvas.setOutline("red")
    canvas.drawText(175,300,"TheOlympics")
    win.wait()    
#finished and it works 

olympicRings()#calling Part two 

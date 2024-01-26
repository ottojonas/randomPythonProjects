#Want to get in a timer to see how many clicks per second, and then have it reset after a certain amount of time 

from tkinter import Tk
import mouse 
#import time

clicks = 0 

def click(): 
    global clicks 
    clicks += 1 
    print(clicks)

root = Tk() 
mouse.on_click(click)
root.mainloop() 
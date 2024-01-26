import mouse 
import keyboard 
import tkinter

clickCount = 0 

def click(): 
    global clickCount
    clickCount += 1
    print("clickCount: ", clickCount)

def onKeyPress(event):
    if event.keysym == "Escape": 
        root.destroy()
    if event.keysym == "space": 
        click() 

def onClick(event): 
    if event.click_type == mouse.ClickTypes.single: 
        click()
        
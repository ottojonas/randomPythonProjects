from tkinter import Tk, Button, Label 
import time 

class clickCounter: 
    def __init__(self, master, timeLimit): 
        self.master = master 
        self.master.title("click counter with timer")
        self.master.geometry("400 x 400")

        self.clicks = 0 
        self.timeLimit = timeLimit
        self.startTime = time.time()
        
        self.labelClicks = Label(self.master, text = "clicks = 0")
        self.labelClicks.pack() 

        self.labelTimer = Label(self.master, text = "time left: {}".format(self.timeLimit))
        self.labelTimer.pack() 

        self.buttonClick = Button(self.master, text = "click here", command = self.click) 
        self.buttonClick.pack()

        self.master.after(1000, self.updateTimer) 

    def clicks(self): 
        self.clicks += 1 
        self.labelClicks.config(text = "clicks: {}".format(self.clicks))
        if self.clicks == 10: 
            self.stopTimer() 

    def updateTimer(self): 
        elapsedTime = int(time.time() - self.starTime)
        timeLeft = max(0, self.timeLimit - elapsedTime)
        self.labelTimer.config(text = "time left: {}".format(timeLeft))
        if timeLeft == 0: 
            self.stopTimer() 
        else: 
            self.master.after(1000, self.updateTimer) 

    def stopTimer(self): 
        self.buttonClick.config(state = "disabled") 
        self.labelTime.config("times up")
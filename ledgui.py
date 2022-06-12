from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

led1 = LED(26)
led2 = LED(19)
led3 = LED(20)


win = Tk()
win.title("LED TOGGLER")
myfont = tkinter.font.Font(family ='Helvetica', size = 12, weight = 'bold')

def YledOn():
    if led1.is_lit:
        led1.off()
        YledButton["text"]= "Turn yellow led On"
    else:
        led1.on()
        YledButton["text"] = "Turn yellow led off"
        
def RledOn():
    if led2.is_lit:
        led2.off()
        RledButton["text"]= "Turn Red led On"
    else:
        led2.on()
        RledButton["text"] = "Turn Red led off"

def GledOn():
    if led3.is_lit:
        led3.off()
        GledButton["text"]= "Turn Green led On"
    else:
        led3.on()
        GledButton["text"] = "Turn Green led off"
        
def exit():
    RPi.GPIO.cleanup()
    win.destroy()
    
YledButton = Button(win, text = "Turn LED on", font = myfont, command = YledOn, bg = "yellow", height = 1, width = 24)
YledButton.grid(row = 0, column = 1)
RledButton = Button(win, text = "Turn LED on", font = myfont, command = RledOn, bg = "red", height = 1, width = 24)
RledButton.grid(row = 0, column = 2)
GledButton = Button(win, text = "Turn LED on", font = myfont, command = GledOn, bg = "green", height = 1, width = 24)
GledButton.grid(row = 0, column = 3)
exButton = Button(win, text = "EXIT", font = myfont, command = exit, bg = "red", height = 1, width = 6)
exButton.grid(row = 2, column = 2)
win.mainloop()
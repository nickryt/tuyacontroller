import tinytuya # https://pypi.org/project/tinytuya/
from tkinter import * 
from tkinter.ttk import *
from tkinter.colorchooser import *
import tkinter as tk
import time

# ------------------------------------------ | TUYA APP INFORMATION

DEVICE_ID = "xxxxx"
IP_ADDRESS = "xxx.xxx.xxx.xxx"
LOCAL_KEY = "xxxxx"
LEDS = None

# ------------------------------------------ | TKINTER GLOBAL VARIABLES

WINDOWSIZE = '500x500'
BACKGROUND = 'white'
root = None

# ------------------------------------------ |  

def pickcolor():
    color = COLORPICKER.show()
    if color != (None, None):
        print("R : " + str(color[0][0]) + "\nG : " + str(color[0][1]) + "\nB : " + str(color[0][2]) + "\n")
        LEDS.set_colour(color[0][0], color[0][1], color[0][2])
        STATUS['text'] = 'SENT COLOR'

# ------------------------------------------ |

def connecttuya():
    global LEDS
    LEDS = tinytuya.BulbDevice(DEVICE_ID, IP_ADDRESS, LOCAL_KEY)
    LEDS.set_version(3.3)
    # data = LEDS.status() 
    # print('Dictionary %r' % data)
    print('got here3')
    STATUS['text'] = 'CONNECTED'
    

# ------------------------------------------ | TKINTER MAIN LOOP

root = tk.Tk()
root.title("LED")
root.geometry(WINDOWSIZE)
root.configure(bg=BACKGROUND)

SELECTIMAGE = tk.PhotoImage(file = "./images/button.png") 
SELECTIMAGE = SELECTIMAGE.zoom(100)
SELECTIMAGE = SELECTIMAGE.subsample(256)
SELECTBUTTON = tk.Button(root, text="Select Color", bg=BACKGROUND, activebackground='white', borderwidth=0, image=SELECTIMAGE, command=pickcolor)
SELECTBUTTON.pack(side=tk.RIGHT, padx=10, pady=10)

COLORPICKER = tk.colorchooser.Chooser(root)

STATUS = tk.Label(root, font=("Arial Bold", 20), text="OFFLINE", bg=BACKGROUND, activebackground='white', foreground='black', borderwidth=0)
STATUS.pack(side=tk.LEFT, padx=10, pady=10)

root.after(1, connecttuya)
root.mainloop()



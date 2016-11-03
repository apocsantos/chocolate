#import RPi.GPIO as GPIO
import os
import sys
import glob
from cryptography.fernet import Fernet
import csv
import Tkinter as tk
from PIL import ImageTk, Image

#This creates the main window of an application
window = tk.Tk()
window.title("Chocolate")
window.geometry("1024x768")
window.configure(background='grey')

path = "bart.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")

#image rotation


#Start the GUI
window.mainloop()

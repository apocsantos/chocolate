###################################################################################################################
#     _____ _                     _       _         _                _            ____       _                    #
#    / ____| |                   | |     | |       | |              | |          |  _ \     | |                   #
#   | |    | |__   ___   ___ ___ | | __ _| |_ ___  | |    _   _  ___| | ___   _  | |_) | ___| |_                  #
#   | |    | '_ \ / _ \ / __/ _ \| |/ _` | __/ _ \ | |   | | | |/ __| |/ / | | | |  _ < / _ \ __|                 #
#   | |____| | | | (_) | (_| (_) | | (_| | ||  __/ | |___| |_| | (__|   <| |_| | | |_) |  __/ |_                  #
#    \_____|_| |_|\___/ \___\___/|_|\__,_|\__\___| |______\__,_|\___|_|\_\\__, | |____/ \___|\__|                 #
#   |  _ \                                                                 __/ |                                  #
#   | |_) |_   _                                                          |___/                                   #
#   |  _ <| | | |                                                                                                 #
#   | |_) | |_| |                                                                                                 #
#   |____/ \__, |                                                                                                 #
#           __/ |                                                                                                 #
#   __     |___/ _ _              _____       _   _____           _      _______                                  #
#   \ \    / /  | | |            |  __ \     | | |  __ \         | |    |__   __|                                 #
#    \ \  / /_ _| | | ___ _   _  | |__) |__ _| |_| |__) |_ _  ___| | __    | | ___  __ _ _ __ ___                 #
#     \ \/ / _` | | |/ _ \ | | | |  _  // _` | __|  ___/ _` |/ __| |/ /    | |/ _ \/ _` | '_ ` _ \                #
#      \  / (_| | | |  __/ |_| | | | \ \ (_| | |_| |  | (_| | (__|   <     | |  __/ (_| | | | | | |               #
#       \/ \__,_|_|_|\___|\__, | |_|  \_\__,_|\__|_|   \__,_|\___|_|\_\    |_|\___|\__,_|_| |_| |_|               #
#                          __/ |                                                                                  #
#                         |___/                                                                                   #
#                                                                                                                 #
###################################################################################################################


####################################################################################
#  ___         _                   ___                     _                       #
# | _ \__ _ __| |____ _ __ _ ___  |_ _|_ __  _ __  ___ _ _| |_ ___                 #
# |  _/ _` / _| / / _` / _` / -_)  | || '  \| '_ \/ _ \ '_|  _(_-<                 #
# |_| \__,_\__|_\_\__,_\__, \___| |___|_|_|_| .__/\___/_|  \__/__/                 #
#                      |___/                |_|                                    #
#                                                                                  #
####################################################################################


#import RPi.GPIO as GPIO
import Tkinter 
from PIL import Image, ImageTk
import time
import sys
import os
import gc
from random import randint


#time to global something
data_list = []
totalimages=0


####################################################################################
#  ___                                 __              _   _                       #
# | _ \_ _ ___  __ _ _ _ __ _ _ __    / _|_  _ _ _  __| |_(_)___ _ _  ___          #
# |  _/ '_/ _ \/ _` | '_/ _` | '  \  |  _| || | ' \/ _|  _| / _ \ ' \(_-<          #
# |_| |_| \___/\__, |_| \__,_|_|_|_| |_|  \_,_|_||_\__|\__|_\___/_||_/__/          #
#              |___/                                                               #
####################################################################################



###############################################################################################################
#                   _                 _    _      _                      _            _                     
#   __ _  _  _|   _|_ o  |  _     _ _|_   (_| o _|__|_ _  _|    o __  _ (_| _  _    _|_   __  _ _|_ o  _ __ 
#   | (/_(_|(_|    |  |  | (/_   (_) |    __| |  |  |_(/_(_|    | |||(_|__|(/__>     | |_|| |(_  |_ | (_)| |
#
###############################################################################################################
#read the list of gift images and the number of gifts for each image
def load_file():
    fp = open('HapppyHippyImages.csv', 'Ur')
    global data_list
    for line in fp:
        data_list.append(line.strip().split(','))
    fp.close()
    #ainda tenho de fazer alteracoes aqui
    counter = data_list[3][1]
    aux=str(int(counter)-1) #decrementa contador
    #ainda falta alterar isto
    #data_list[3][1] = aux #coloca o valor na lista
#End of function

###################################################################################
#                     _                     _         
#   _  _     _       |_) _| _ _|_ _  _|   _|_ o  |  _ 
#  _> (_|\_/(/_   |_||  (_|(_| |_(/_(_|    |  |  | (/_
###################################################################################
#write the list of gift images and the number of gifts ||left|| for each image
def save_file():
        global data_list
        fp = open('HapppyHippyImages.csv', 'w')
        for line in data_list:
                fp.write(','.join(line) + '\n')
        fp.close()
#End of function


###################################################################################
#      _                          _         _                     
#     |_) _| _ _|_ _     o __  _ (_| _    _|_   __  _ _|_ o  _ __ 
#  |_||  (_|(_| |_(/_    | |||(_|__|(/_    | |_|| |(_  |_ | (_)| |
###################################################################################
    
def update_image():
        global tkimg1
        global data_list
        currentImage = randint(0,len(data_list))
        tkimg1 = ImageTk.PhotoImage(Image.open(data_list[currentImage][0]))
        label.config( image = tkimg1)
        label.after(1000, update_image)
        print "Updated"


###################################################################################
#  ____ ____ ____ ___ ____ ____ ___    ____ _  _ _  _ ____ ___ _ ____ _  _ 
#  |__/ |___ [__   |  |__| |__/  |     |___ |  | |\ | |     |  | |  | |\ | 
#  |  \ |___ ___]  |  |  | |  \  |     |    |__| | \| |___  |  | |__| | \| 
#                                                                          
###################################################################################
def restart_program():
        gc.collect()
        python = sys.executable
        os.execl(python, python, * sys.argv)

###################################################################################
#   )_/  _           _   _ _   _  _   _   _ )   _(_      _   _ _)_ o  _   _  
#  /  ) )_) (_(     )_) ) )_) (  (   )_) (_(      ) (_( ) ) (_ (_  ( (_) ) ) 
#      (_     _)   (     (_   _) _) (_                                       
###################################################################################
def keypress(event):
        global data_list
        x = event.char
        if x == "p":
                time.sleep(5) #pause the program for 30 seconds
                print "p pressed" #for debuggin purposes
                #loop for comparisation
                for i, val in enumerate(data_list):
                        print data_list[i][1]
                        if(data_list[i][0] == 'bear.jpg'): #to be changed and receive the current file name
                                counter = data_list[i][1] #compare
                                aux=str(int(counter)-1) #decrementa contador
                                data_list[i][1] = aux #coloca o valor na lista
                                print data_list[i][1] #for debugging purposes
                        else:
                                print "keyPressed" #for debuggin purposes
                                restart_program() #restarts the program


###############################################################
#                                                             #
#    __  __      _        ___                                 #
#   |  \/  |__ _(_)_ _   | _ \_ _ ___  __ _ _ _ __ _ _ __     #
#   | |\/| / _` | | ' \  |  _/ '_/ _ \/ _` | '_/ _` | '  \    #
#   |_|  |_\__,_|_|_||_| |_| |_| \___/\__, |_| \__,_|_|_|_|   #
#                                     |___/                   #
#                                                             #
###############################################################

#load the gift image file
load_file()
 
#This creates the main window of an application
w = Tkinter.Tk()
w.title("Chocolate")
w.geometry("1024x768")
w.configure(background='grey')
im = Image.open('bear.jpg')
tkimg1 = ImageTk.PhotoImage(im)
label =  Tkinter.Label(w, image=tkimg1)
#for debugging only
print "Loaded"
#end of debugging

#main program

label.pack()
w.after(1000, update_image)
#key
print "Press a key (Escape key to exit):"
w.bind_all('<Key>', keypress)
#endkey

#main loop
w.mainloop()

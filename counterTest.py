#import RPi.GPIO as GPIO
import os
import sys
import glob
import csv



#read counter function
with open('conter.csv', 'rb') as f:
    counter = f.readline()
    f.close()
    

#write counter function
valor = (int(counter)+1)
print valor
f = open( 'conter.csv', 'w' )
f.write(str(valor))
f.close()

#cipher_suite = Fernet("TheFrickiongKey")
#cipher_text = cipher_suite.encrypt("text")
#plain_text = cipher_suite.decrypt(cipher_text)

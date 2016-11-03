#import RPi.GPIO as GPIO
import os
import sys
import glob
#from cryptography.fernet import Fernet
import csv


#cria uma lista
file_list = []
#le os ficheiros para uma lista
for name in glob.glob('*'):
    file_list.append(name);

#grava o nome das imagens numa lista
csvfile = "listaImagens.csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in file_list:
        writer.writerow([val])    


#cipher_suite = Fernet("TheFrickiongKey")
#cipher_text = cipher_suite.encrypt("text")
#plain_text = cipher_suite.decrypt(cipher_text)

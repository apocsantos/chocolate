#import RPi.GPIO as GPIO
import os
import sys
#from PIL import Image
import glob
#from cryptography.fernet import Fernet
import csv


#cria uma lista
file_list = []
#le o nome dos ficheiros das imagens premiadas e a frequencia minima
imgNumber = input("numero de imagens premiadas a inserir: ")

for x in range(0, imgNumber):
    imgName = raw_input("Nome da imagem: ")
    frequ = raw_input("Frequencia minima para repetir: ")
    data = imgName + "," + frequ
    file_list.append(data)
    

#grava o nome das imagens numa lista
csvfile = "HapppyHippyImages.csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output, delimiter=',' , lineterminator='\n')
    for val in file_list:
        writer.writerow([val])    


#cipher_suite = Fernet("TheFrickiongKey")
#cipher_text = cipher_suite.encrypt("text")
#plain_text = cipher_suite.decrypt(cipher_text)

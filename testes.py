import csv

#with open('HapppyHippyImages.csv') as csvfile:
with open('HapppyHippyImages.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         print(row[0], row[1])   

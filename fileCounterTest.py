
#read the list of gift images and the number of gifts for each image
def load_file():
    fp = open('HapppyHippyImages.csv', 'Ur')
    data_list = []
    for line in fp:
        data_list.append(line.strip().split(','))
    fp.close()
    counter = data_list[3][1]
    aux=str(int(counter)-1) #decrementa contador
    data_list[3][1] = aux #coloca o valor na lista
#End of function


#loop for comparisation
for i, val in enumerate(data_list):
    #print data_list[i][1]
    if(data_list[i][0] == 'bear.jpg'):
        counter = data_list[i][1]
        aux=str(int(counter)-1) #decrementa contador
        data_list[i][1] = aux #coloca o valor na lista
        print data_list[i][1]



#write the list of gift images and the number of gifts ||left|| for each image
#def save_file(filename, data_list):
def save_file():
    fp = open('HapppyHippyImages.csv', 'w')
    for line in data_list:
        fp.write(','.join(line) + '\n')
    fp.close()
#End of function

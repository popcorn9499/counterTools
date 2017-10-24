import json

fileName = "test.txt"

def fileSave(fileName,config):
    print("Saving")
    f = open(fileName, 'w') #opens the file your saving to with write permissions
    f.write(config) #writes the string to a file
    f.close() #closes the file io

def fileLoad(fileName):#loads files
    print(open(fileName, 'r').read())
    with open(fileName, 'r') as handle:#loads the json file
        print(handle)
    return open(fileName, 'r').read()
    

#this loads the file    
x = fileLoad(fileName)
#splits it to a list
x = x.split()
#increments the counter value
x[1] = int(x[1]) +  1
new = ""
#saves the list back to a file
for i in x:
    new = new + str(i) + "\r\n"

#saves the final file
fileSave(fileName,new)

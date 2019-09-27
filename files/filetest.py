# Testing reading, opening and writing files
import os
import os.path
#from os.path import path


def checkFile(path, mode='r'):
    if path.exist("hej.txt"):
        openFile()
    else: 
        f= open("hej.txt","w+")
        openFile()


def openFile():
    with open("hej.txt", "r") as file:
        for line in file:
            print(f"rad i filen:{line}")
#            writeFile()

#def writeFile():
#    with open("createFile.txt", "w") as file:
#        file.write("Hej\n");
#        file.write("Hejs\n");
#        file.write("HejZ\n");
        
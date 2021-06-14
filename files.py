#Kaden Alibhai 6/14/2021
#We are going to learn how to use files
import os
import sys
import time

#using time to pause the game

print("Hello")
time.sleep(2)
print("there")
def readFile():
    file= input("What is the name of the file? ")
    if os.path.exists(file):
        #it opens the file
        PEN=open(file, 'r')
        #prints the whole file
        print(PEN.read())
        PEN.close()
    else:
        print("The file does not exist! Thank you")

fileNAME="KadenGAME.txt"
if os.path.exists(fileNAME):
    print("sorry that file exists")
else:
    FILE=open(fileNAME, 'w')
    FILE.write("******     THIS IS KADEN's FILE    ******")
    FILE.close()
    time.sleep(1)
    FILE=open(fileNAME, 'r')
    print(FILE.read())
    FILE.close
File=open("KadenGAME.txt", 'a')
newline="\n What ever"
File.write(newline)
File.close()
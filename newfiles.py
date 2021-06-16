# Kaden Alibhai
# 6/16/21
# we are going to learn how to open files, read files, write files 
# How to read files per line 
# How to make a list from file 
# How to manipulate the elements to find what we need 


import os
import sys
import time
os.system('cls')


file="asdfre.txt"
FILE=open(file, 'r')
content=FILE.read()
print(content)
FILE=open(file,'r')
content_List=FILE.readlines()
print(content_List)
FILE.close()
for element in content_List:
    print("line : ", element)
    elem_list=element.split()
    print(elem_list)
    time.sleep(1)

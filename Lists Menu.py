#Kaden Alibhai 6/10/21
#Challenge 3 
#5 elements that change a list
# 1 insert elements either appending or inserting
# 2 delete an element either by value or by index
# 3  find if something in the list
# 4  Find the index where an element is in the list
# 5 reverse th eorder of the array

from os import X_OK


l1= "***************************************"
l2= "*           Lists Game                *"
l3= "*                                     *"
l4= "*    1 - Insert Element               *"
l5= "*    2 - Delete Element               *"
l6= "*    3 - Find Element                 *"
l7= "*    4 - Index Element                *"
l8= "*    5 - Reverse Order                *"
l9= "*    6 - Exit Game                    *"
l10="*  List: MJ, Lebron, Curry, KD, Kawhi *"
l11="***************************************"
x=1
def menu():
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l8)
    print(l9)
    print(l10)
    print(l11)
    print("please enter your selection from 1 to 6")
    inputNumber = input()
    x = int(inputNumber)
    return x


def pause():
    print("Do you want to play again?")
    var=input()
    var=var.upper()
    if "Y" in var:
        return True
    else:
        return False

Playerslist=["MJ", "Lebron", "Curry", "KD", "Kawhi"]


def addELEMENT():
    print("Add element to list")
    print("What basketball player do you want to add?")
    answer=input()
    print("What posititon 0-4 in the list do you want it?")
    answer1=int(input())
    Playerslist.insert(answer1, answer)
    print("Here is the new list")
    print(Playerslist)

def deleteELEMENT():
    print("Delete an element from the list")
    print("Which player would you like to remove?")
    print(Playerslist)
    answer=input()
    Playerslist.remove(answer)
    print("Here is the new list")
    print(Playerslist)

def findELEMENT():
    print ("Find an element in the list")
    print("What would you like to find in the list")
    print(Playerslist)
    answer=input()
    if answer=="MJ":
        print("What you entered is in the list")
    elif answer =="Lebron":
        print("What you entered is in the list")
    elif answer=="KD":
        print("What you entered is in the list")
    elif answer=="Curry":
        print("What you entered is in the list")
    elif answer=="Kawhi":
        print("What you entered is in the list")
    else:
        print("What you entered is not in the list")

def indexELEMENT():
    print("Find the index of an element")
    print(Playerslist)
    print("Enter the element you want indexed")
    answer= str(input())
    print(Playerslist.index(answer))

def reverseLIST():
    print("Reverse the order of the list")
    print(Playerslist)
    print("Press enter to reverse the order of the list")
    answer=input()
    Playerslist.reverse()
    print(Playerslist)

while x !=6:
    x=menu()
    if (x==1):
        convert=True
        while convert:
            addELEMENT()
            convert=pause()
    
    if (x==2):
        convert=True
        while convert:
            deleteELEMENT()
            convert=pause()
    
    if (x==3):
        convert=True
        while convert:
            findELEMENT()
            convert=pause()
    
    if (x==4):
        convert=True
        while convert:
            indexELEMENT()
            convert=pause()

    if (x==5):
        convert=True
        while convert:
            reverseLIST()
            convert=pause()
    
    if (x==6):
        print("Goodbye, thank you for playing")
    
    

           
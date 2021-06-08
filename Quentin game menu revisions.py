#Kaden Alibhai 6/8/21
#Today I will be revising Quentin's game menu
#while loop
#condtional if
#Functions are peices of code that we can reuse
#to declare a function we must use the keyword def give a name

#Global variables can be used anywhere in the program
l1="**************************"
l2="*       My game          *"
l3="*                        *"
l4="*    1 - Level1          *"
l5="*    2 - Level2          *"
l6="*    3 - Scores          *"
l7="*    4 - Exit Game       *"
l8="**************************"
x=1  #global variable
def menu():
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l8)
    print("please enter your selection from 1 to 4")
    inputNumber = input()
    x = int(inputNumber)
    return x
def score():
    print(l1)
    print("*        Scores          *")
    print(l3)
    print("*    1 - ???- 999        *")
    print("*    2 - ???- 876        *")
    print("*    3 - ???- 745        *")
    print(l3)
    print(l8)
while x !=4:  
    x=menu()
    if(x==1):        #if statement are selection or branching
        print("Level 1 Chosen")

    if(x==2):
        print("Level 2 Chosen")

    if(x==3):
        score()


print("Goodbye, Thank you for playing")
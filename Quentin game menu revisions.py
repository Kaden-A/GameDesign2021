#Kaden Alibhai 6/8/21
#Today I will be revising Quentin's game menu
#while loop
#condtional if
#Functions are peices of code that we can reuse
#to declare a function we must use the keyword def give a name

#Global variables can be used anywhere in the program
l1= "***************************************"
l2= "*           Strings Game              *"
l3= "*                                     *"
l4= "*    1 - Capitalize                   *"
l5= "*    2 - Uppercase                    *"
l6= "*    3 - Lowercase                    *"
l7= "*    4 - Find index of character      *"
l8= "*    5 - Split                        *"
l9= "*    6 - Translate                    *"
l10="*    7 - Exit Game                    *"
l11="***************************************"
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
    print(l9)
    print(l10)
    print(l11)
    print("please enter your selection from 1 to 7")
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
def pause():
    print("Do you want to play again?")
    var=input()
    var=var.upper()
    if "Y" in var:
        return True
    else:
        return False

while x !=7:  #loop is conditioned to an event
    x=menu()
    if(x==1):  #if statement are selection or branching
        convert=True
        while convert:  #let the user stay in the level and reuse it many times until they want to go back to the menu
            print("Level 1 chosen")   
            print("Please enter a phrase in lower case")
            answer=input()   #input is a function
            print(answer.capitalize()) #is a method of strings and you have referred with "."
            answer=answer.capitalize() #update variable to the new changed if i dont need original value
            convert=pause()
        

    if(x==2):
        convert=True
        while convert:
            print("Input a phrase with lower case letters")
            answer=input()
            print(answer.upper())
            answer=answer.upper()
            pause()

    if(x==3):
        convert=True
        while convert:
            print("Please enter a phrase in upper case")
            answer=input()
            print(answer.lower())
            pause()
    
    if(x==4):
        convert=True
        while convert:
            print("Enter a phrase")
            phrase=input()
            print("Enter the character you want to find")
            answer=input()
            print(phrase.find(answer))
            pause()
    
    if(x==5):
        convert=True
        while convert:
            print("Enter the string you want to be split")
            answer=input()
            print(answer.split())
            pause()
    
    if(x==6):
        convert=True
        while convert:
            print("Input the phrase you would like to translate")
            answer=input()
            var1=answer.maketrans("a","X")
            print(answer.translate(var1))
            pause()
    
    if(x==7):
        print("Thank you for playing")
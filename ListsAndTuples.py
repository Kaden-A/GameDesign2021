#Kaden Alibhai 6/10/2021
#We are learning about lists and tuples
#Learn their functions and looping with lists

#How to use a module or library by importing
import random

myFruit=["apples", "berries", "mangos", "bananas"]
print(myFruit)
for fruit in myFruit:
    print(fruit)
    
for fruit in myFruit: #for the length of your array
    print(fruit, end=" , ")
print()
counter=len(myFruit) #The length of the list is one more than the last index
#finding a random number to be the index to select randint()
indx= random.randint(0,counter-1)
print("your lucky fruit is ", myFruit[indx])

#random method choice()
word=random.choice(myFruit)
print("Your random fruit is ", word)

for x in range(0,counter-1):
    print(myFruit[x], end=" , ")

print(myFruit[counter-1]) #print the last element

if "apples" in myFruit:
    print("Yes you got apples")
    myFruit.remove("apples")
    print(myFruit)
myFruit.insert(0,"kiwi")
myFruit.insert(2,"papaya")
myFruit.append("beets")
print(myFruit)

fruity=("apple", "pears", "banana") #tuple
print("tuple",fruity)
temp= list (fruity) #temp is a list
print("list",temp)
temp.insert(1,"kiwi")
fruity=tuple(temp)
print("tuple modified", fruity)
print("list modified", temp)
for element in fruity:
    print(element)
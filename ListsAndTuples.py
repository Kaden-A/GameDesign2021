#Kaden Alibhai 6/10/2021
#We are learning about lists and tuples
#Learn their functions and looping with lists
myFruit=["apples", "berries", "mangos", "bananas"]
print(myFruit)
for fruit in myFruit:
    print(fruit)
    
for fruit in myFruit: #for the length of your array
    print(fruit, end=" , ")
print()
counter=len(myFruit) #The length of the list is one more than the last index

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

#Kaden Alibhai
#We are going to print a multiplication table for 2
# Using print statement
# input --> variable is a container to keep data and
# they need to have valid and unique name and they will have a unique value
base = 2
var2 = 7
print (1 * base)
print (2 * base)
print (3 * base)
print (4 * base)
print (5 * base)
print (6 * base)
print (7 * base)
print (8 * base)
print (9 * base)
print (10 * base)
# repetition I should think looping exact number for statement
for i in range(1,11):  #beginning of range is included end of range is not 
    print(i * base, end= "  ")
base = 3
print()
for i in range(1,11):  #beginning of range is included end of range is not 
    print(i * base, end= "  ")
base =4
print()
for i in range(1,11):  #beginning of range is included end of range is not 
    print(i * base, end= "  ")
    # when we have several repetitions then we can use veral loops
    #sometimes they can be nested loops
for var in range(1, 11):
    print()
    for i in range (1, 11):
        print (i * var,  end= "   ")
     
    
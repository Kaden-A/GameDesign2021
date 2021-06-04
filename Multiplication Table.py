#Kaden Alibhai
#6/4/2021
#We are going to print multiplication tables
#Asking the user which table
#input --> input()
print("What is the base?")
base=int(input())
print(type(base))
print("Multiplication Table",base)
print()
for var in range (1,11):
    resolved=base*var
    print(base, 'x', var, '=', resolved)


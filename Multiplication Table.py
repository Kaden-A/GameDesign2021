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
print("What is the base?")
base=int(input())
print(type(base))
print("Addition Table",base)
print()
for var in range (1,11):
    resolved=base+var
    print(base, '+', var, '=', resolved)
print("What is the base?")
base=int(input())
print(type(base))
print("Division Table",base)
print()
for var in range (1,11):
    resolved=base/var
    print(base, '/', var, '=', resolved)
print("What is the base?")
base=int(input())
print(type(base))
print("Subtraction Table",base)
print()
for var in range (1,11):
    resolved=base-var
    print(base, '-', var, '=', resolved)

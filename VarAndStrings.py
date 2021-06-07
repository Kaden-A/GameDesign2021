#Kaden Alibhai 6/7/21
#We are learning how to work with strings
#While loop
#Different type of var

num1=19
num2=3.5
num3=0x2342FABCDEBDA
#How to know what type of date is a variable
print(type(num1))
print(type(num2))
print(type(num3))
phrase="Hello there!"
print(type(phrase))
#String functions
num=len(phrase)
print(phrase[3:7]) #from 3 to 6
print(phrase[6:])  #from index to the end
print(phrase*2)    #print it twice
#concadentation --> joining strings
phrase = phrase + "Goodbye"
print(phrase)
print(phrase[2:num-1])
while "there" in phrase:
    print("there" in phrase)
    phrase="changed"
    print(phrase)
# make 3 string variables print them individually
#"print s1+s2"
#print st2+st3
#print st1+st2+st3
phrase1="Lebron"
phrase2=">"
phrase3="MJ"
print(phrase1)
print(phrase2)
print(phrase3)
print(phrase1+phrase2)
print(phrase2+phrase3)
print(phrase1+ " ", phrase2+ " ",phrase3)
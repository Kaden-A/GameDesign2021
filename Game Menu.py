print("***********************")
print("*        Run          *")
print("*        Menu         *")
print("*                     *")
print("*   1.-Easy           *")
print("*   2.-Medium         *")
print("*   3.-Hard           *")
print("*   4.-High Scores    *")
print("*   5.-End Game       *")
print("***********************")
answer=(input())
while "5" in answer:
    print("Error: Cannot perform the requested operation at this time")
    answer="changed"
print("Would you like to exit the game?")
answer=(input())
while "no" in answer:
    print("***********************")
    print("*        Run          *")
    print("*        Menu         *")
    print("*                     *")
    print("*   1.-Easy           *")
    print("*   2.-Medium         *")
    print("*   3.-Hard           *")
    print("*   4.-High Scores    *")
    print("*   5.-End Game       *")
    print("***********************")
    answer=(input())
while "yes" in answer:
    txt= "thank you for playing"
    x=txt.capitalize()
    print(x)
    answer="changed"
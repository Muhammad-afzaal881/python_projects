import random
computer = random.randint(0,100)
a = -1
guess = 0
while(a != computer):
    guess+=1
    a =int(input("GUESS THE NO"))
    if(a > computer):
        print("enter lower value")
    elif(a < computer):
        print("enter higher value")
print(f"You are win {computer} and {guess} attempt")        

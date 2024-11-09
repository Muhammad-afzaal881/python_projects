# Stone paper siser game
import random
computer =random.choice([0,1,-1])
user = input("Enter your choice")
dic = {"stone": 0,"paper": -1,"siser":1}
comdic = {0: "stone",-1 :"paper",1:"siser"}
afz =dic[user]
print(f"Your choice {comdic[afz]}\n computer choice s{comdic[computer]}")
if(computer==-1 and afz==-1):
    print("try again")
elif(computer==-1 and afz==1):
    print("you win")
elif(computer==-1 and afz==0):
    print("you lose")
elif(computer==1 and afz==1):
    print("try again")
elif(computer==1 and afz==0):
    print("you win")     
elif(computer==1 and afz==-1):
    print("you win")
elif(computer==0 and afz==0):
    print("try again")
elif(computer==0 and afz==-1):
    print("you win")             
elif(computer==0 and afz==1):
    print("you lose")
else:
    print("stone paper siser")    

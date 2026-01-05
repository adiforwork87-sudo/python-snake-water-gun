# Snake water gun game 
# Author : Aditya Kumar 
import random 
'''
1 for snake 
-1 for water 
0 for gun 
'''
computer = random.choice([-1,0,1])

Youstr = input("Enter your choice:")

YouDict = {"s":1, "w":-1, "g":0} 

if Youstr not in YouDict:
    print("Invalid input! Please enter s, w, or g")
    exit()



ReverseDict = {1:"snake",-1:"water",0:"gun"}

You = YouDict[Youstr]

# By now We have 2 numbers (Variable) , you and computer 
print(f"You chose {ReverseDict[You]}\nComputer chose {ReverseDict[computer]}")
  
if ( computer == You):
    print("its a draw")
else:
    if ( computer == -1 and You ==1):
        print("You Win!")
    elif( computer == -1 and You ==0):
        print("You Lose!")    
    elif( computer == 1 and You ==-1):
        print("You Lose!")     
    elif( computer == 1 and You ==0):
        print("You Win!")  
    elif( computer == 0 and You ==1):
        print("You Lose!")  
    elif( computer == 0 and You ==-1):
        print("You Win!")  
    else:
        print("Something went wrong!")
                                                    

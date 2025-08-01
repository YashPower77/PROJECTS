print("WELCOME TO THE PERFECT GUESS GAME")
import random
number = random.randint(1,100)
user_number = None
guess = 0
while (user_number!= number):
    user_number = int(input("ENTER YOUR NUMBER FOR GUESS  : "))
    guess +=1
    if(user_number>number):
        print(f"SORRY \nTHINK SMALLER THAN YOU THINK")

    elif(user_number<number):
        print(f"OOPS \nTHINK LARGE NUMBER")
        

    else:
        print(f"CONGRUTS , \nYOUR GUESS IS PERFECT")
      

print(f"THE PERFECT NUMBER IS {number} AND YOU TAKE {guess} TO GUESS THE NUMBER")    

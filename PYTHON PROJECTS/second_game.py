import random

while True:
    print("WELCOME TO THE SNAKE-WATER-GUN GAME  ")
    print("1 - SNAKE")
    print("2 - WATER")
    print("3 - GUN")

    user_choice= int(input("Enter your choice  :"))
    if user_choice==1:
        user = "snake"

    elif user_choice==2:
        user = "water"

    elif user_choice==3:
        user = "gun"

    else:
        print("INVAILD CHOICE")   
        continue 
    
    computer = random.choice(["snake" , "water" ,"gun"])
    print(f"computer choice is {computer}")

    if(computer==user):
        print("It is a tie game") 

    elif(user == "snake" and computer=="water") or \
        (user == "water" and computer=="gun") or \
        (user == "gun" and computer=="snake"):
        print("You win")  

    else:
        print("computer wins ") 
       

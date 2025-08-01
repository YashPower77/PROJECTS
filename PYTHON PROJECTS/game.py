import random

print ("WELCOME TO THE ROCK - PAPER - SCISSORS GAME ")
print(" CHOOSE ONE OPTION")
print("1 - ROCK")
print("2 - PAPER")
print("3 - SCISSORS")

user_score = 0
computer_score = 0

while True:
    user_choice = int(input("enter your choice : "))
    
    if user_choice==1:
        user = "rock"
    elif user_choice==2:
        user = "paper"    
    elif user_choice==3:
        user = "scissor"

    else:
        print("INVAILD CHOICE")
        continue

    computer = random.choice(["rock", "paper", "scissor"])
    print(f"computer choice : {computer}")

    if user == computer:
        print ("it is a tie")
    elif(user == "rock" and computer=="scissor") or \
        (user == "paper" and computer=="rock") or \
        (user == "scissor" and computer=="paper"):
        print("you win this round!")
        computer_score+=1

        print(f"Score : You = {user_score} | Computer = {computer_score}")

        again = input("Do you want to play again? (yes/no) : ")
        if again != "yes":
            print("thanks for playing")
            break

            
                   
import random

tryAgain = True
chance = 3
print("Rock, Paper, Scissor Game")
print("=========================")
while tryAgain:
    player = input("Choose one : |rock| |paper| |scissor| \nyour choice :")
    computer = random.random()
    if computer < 0.34:
        computer = "rock"
    elif computer >= 0.34 and computer < 0.67:
        computer = "paper"
    else:
        computer = "scissor"
        
    if player == computer:
        result = "Draw!"
    elif player == "rock":
        if computer == "paper":
            result = "You Lose!"
        else:
            result = "You Win!"
    elif player == "paper":
        if computer == "rock":
            result = "You Win!"
        else:
            result = "You Lose!"
    elif player == "scissor":
        if computer == "Rock":
            result = "You Lose!"
        else:
            result = "You Win!"
    else:
        print("please fill with correct option!")
        result = "error"
    chance -= 1    
    print("you choice is "+player+" and your enemy choice is "+computer+ "\nthe result is "+result)
    print("remaining chance = "+str(chance)+"x")
    
    if chance == 0:
        repeat = True
        while repeat:
            confirm = input("Try Again? (y/n) : ")
            if confirm == "y":
                tryAgain
                repeat = False
                chance = 3
            elif confirm == "n":
                tryAgain = False
                repeat = False
            else:
                print("please fill with correct option!")
        
print("Thanks for playing!")
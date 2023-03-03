print('hi Dennis ')
import random

print("Welcome to Rock-Paper-Scissors!")
print("Game Rules: ")
print(
"""1. Rock beats Scissors
2. Scissors beats Paper
3. Paper beats Rock
""")
print('===============================')
# pilihan yg tersedia
choices = ["rock", "paper", "scissors"]

# inputan player (lower(): untuk mengkonversi huruf menjadi kecil )
play_choice = input("Please choose rock, paper, or scissors: ").lower()

# pilihan komputer (random.choice(): memilih acak elemen pada variabel)
com_choice = random.choice(choices)

# Hasil
print('===============================')
print(f"\nYou choose {play_choice}")
print(f"The computer chose {com_choice}\n")

# Kondisi
if play_choice == com_choice:
    print("Draw!!!")
elif (play_choice == "rock" and com_choice == "scissors") or 
     (play_choice == "scissors" and com_choice == "paper") or 
     (play_choice == "paper" and com_choice == "rock"):
    print("Player Win!!!")
else:
    print("Computer Win!!!.")




import random

print("~~~~~ WELCOME TO ROCK PAPER SCISSORS GAME ~~~~~")

user_score = 0
computer_score = 0
ties = 0

name = input("Enter Your Good Name Here: ")
print("""
~~ Winning Rules ~~
1. Rock vs Paper --> Paper Win 
2. Paper vs Scissors --> Scissors Win
3. Rock vs Scissors --> Rock Win""")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print("""Choices Are: 
1. Rock
2. Paper
3. Scissors""")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
choice = int(input("Enter Your Choice From 1-3: "))
print()
while choice > 3 or choice < 1:
    choice = int(input("Enter Valid Input: "))

if choice == 1:
    user_choice = 'Rock'
elif choice == 2:
    user_choice = 'Paper'
else:
    user_choice = 'Scissors'
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print("The User's Choice = ", user_choice)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print("Now it is Computer's Turn: ")

computer = random.randint(1,3)

if computer == 1:
    computer_choice = 'Rock'
elif computer == 2:
    computer_choice = 'Paper'
else:
    computer_choice = 'Scissors'

print("The Computer's Choice = ", computer_choice)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
if((user_choice == 'Paper' and computer_choice == 'Rock') or (user_choice == 'Rock' and computer_choice == 'Paper')):
    print('Paper Wins')
    result = 'Paper'
elif((user_choice == 'Scissors' and computer_choice == 'Rock') or (user_choice == 'Rock' and computer_choice == 'Scissors')):
    print('Rock Wins')
    result = 'Rock'
elif(user_choice == computer_choice):
    print("It's a TIE")
    result = 'TIE'
else:
    print("Scissors Wins")
    result = "Scissors"

if result == 'TIE':
    ties +=1
elif result == user_choice:
    print("User Wins")
    user_score += 1
else:
    print("~~~ Computer Wins ~~~")
    computer_score += 1
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print("Scores Are: ")
print(name,"'s Score = ",user_score)
print("Computer's Score = ", computer_score)
print("Ties Are =: ", ties)

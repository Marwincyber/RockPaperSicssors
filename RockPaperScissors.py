import random
#Print multiline instruction
print("Winning rules of the game ROCK PAPER SCISSORS are:\n")
print("Rock vs Paper -> Paper wins \n")
print("Rock vs Scissors -> Rock wins \n")
print("Paper vs Scissors -> Scissors wins")
while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3-Scissors \n")
    choice = int(input("Enter your choice: "))
    while choice> 3 or choice <1:
        choice= int(input("Enter a valid choice please 🥲 "))
    if choice == 1:
        player_choice = 'Rock'
    elif choice == 2:
        player_choice='Paper'
    else:
        player_choice='Scissors'
    print('User choice is:', player_choice)
    print("Now it's Computer's Turn...")
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice = 'Rock'
    elif computer_choice == 2:
        computer_choice = 'Paper'
    else:
        computer_choice = 'Scissors'
    print("Computer choice is:", computer_choice)
    print(player_choice, 'vs', computer_choice)
    if player_choice == computer_choice:
        result = "Draw"
    elif (player_choice == 1 and computer_choice == 2) or (computer_choice == 1 and player_choice == 2):
        result = 'Paper'
    elif (player_choice == 1 and computer_choice == 3) or (computer_choice == 1 and player_choice == 3):
        result = 'Rock'  
    elif (player_choice == 2 and computer_choice == 3) or (computer_choice == 2 and player_choice == 3):
        result = 'Scissors'
    if result == 'Draw':
        print("<==It's a tie==>")
    elif result == player_choice:
        print("<==You win!==>")
    else:
        print("<==Computer wins!==>")
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
print("Thanks for playing!")

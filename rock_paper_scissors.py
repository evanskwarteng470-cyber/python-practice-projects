import random

print("Welcome to Rock Paper Scissors!")

choices = ["rock", "paper", "scissors",]

player_score = 0
computer_score = 0

while True:
    player = input("\nEnter rock, paper or scissors: ").lower()

    if player not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if player == computer:
     print("It's a tie!")

    elif (
    (player == "rock" and computer == "scissors") or 
    (player == "paper" and computer == "rock") or
    (player == "scissors" and computer == "paper")
    ):
        print("You win!")
        player_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("Your score", player_score)
    print("Computer score", computer_score)

    play_again = input("Play again? (yes/no):").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break




                                                  

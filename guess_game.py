import random

print("Welcome to the guessing game!")

while True:
    print("\nSelect Difficulty:")
    print("1. Easy (10 attempts)")
    print("2. Medium (5 attempts)")
    print("3. Hard (3 attempts)")

    
    choice = input("Enter choice (1/2/3):")


    if choice == "1":
        max_attempts = 10
    elif choice == "2":
        max_attempts = 5
    elif choice == "3":
        max_attempts = 3
    else:
        print("Invalid choice! Defaulting to the medium.")
        max_attempts = 5


    number = random.randint(1, 100)
    attempts = 0

    print("\nI am thinking of a number between 1 and 100.")
    print("You have", max_attempts, "attempts")

    won = False

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess:"))
            attempts += 1

            difference = abs(number - guess)


            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print("Correct! you won!")
                won = True
                break


            difference = abs(number - guess)

            if difference <= 5:
                print("Very close!")
            elif difference <= 15:
                print("Getting closer!")
            else:
                print("Far away!")

            print("Atteempts left:", max_attempts - attempts)

            if attempts == max_attempts and guess != number:
                print("You lost! The number was: ", number)

              


        except ValueError:
            print("Please enter a valid number!")


            if attempts == max_attempts and guess != number:
                print("You lost! The number was:", number)


            play_again = input("Do you want to play again? (yes/no):").lower()
            if play_again != "yes":
                print("Thanks for playing")
                break
                
score = 0

print("Welcome to the Quiz Game!")
print()

answer = input("1. What is the capital of Ghana?")

if answer.lower() == "accra":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Accra.")

print()

answer = input("2. How many regions does Ghana have?")

if answer == "16":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is 16.")

print()

answer = input("3. What is 5*6?")

if answer == "30":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is 3o.")

print()
print("Final score:", score, "/3")

if score == 3:
    print("Excellent!")
elif score == 2:
    print("Good job!")
else:
    print("Keep practicing!")

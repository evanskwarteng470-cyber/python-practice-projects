questions = [
    "What is the capital of Ghana?",
    "How many regions does Ghana have?",
    "What is 5*6?",
    "What is the largest planet in our solar system?"
]

answers =  [
    "accra",
    "16",
    "30",
    "jupiter"
]

score = 0

print("Welcome to the quiz game!")
print()

for i in range(len(questions)):
    user_answer = input(questions[i] + " ")

    if user_answer.lower() == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    print("Final score:", score, "/", len(questions) )

    if score == len(questions):
        print("Excellent!")
    elif score >= 2:
        print("Good job!")
    else:
        print("Keep practicing!")

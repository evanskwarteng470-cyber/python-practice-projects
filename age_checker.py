while True:
    name = input("What is your name?")
    age = int(input("How old are you?"))

    print("Hello",name)
    print("you are", age, "years old")

    if age < 13:
        print("you are a child")
    elif age < 18:
        print("You are a teenager")
    else:
        print("you are an adult")

        again = input ("Do you want to try again?(yes/no):")
        if again.lower() =="no":
            print("Good bye")
            break



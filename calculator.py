while True:
    print("Mini calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

    choice = input("Choose an option (1/2/3/4/):").strip()
    
    if choice not in ["1","2","3","4"]:
        print("Invalid choice")
        continue

    try:
        num1 = float(input("Enter first number"))
        num2 = float(input("Enter second number"))
    except ValueError:
        print("Error: please enter valid numbers")
        continue

    if choice == "1":
        print("Ressult =", num1 + num2)
    elif choice == "2":
        print("Result =", num1 - num2)
    elif choice == "3":
        print("Result =", num1 * num2)
    elif choice == "4":
        if num2 == 0:
            print("Error: cannot divide by zero")
        else:
            print("Result =", num1 / num2)

    again = input("Do you want to calculate again?(yes/no)")
    if again.lower() == "no":
        print("Good bye")
        break

 
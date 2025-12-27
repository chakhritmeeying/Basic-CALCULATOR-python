print("CALCULATOR")
main_loop = True

while main_loop:
    try:
        number_1 = float(input("Enter 1st number: "))
        number_2 = float(input("Enter 2nd number: "))
    except ValueError:
        print("Please enter number.")
        continue
    operator = input("Enter the operator[+,-,*,/]: ")

    if operator == '+':
        result = number_1 + number_2
    elif operator == '-':
        result = number_1 - number_2
    elif operator == '*':
        result = number_1 * number_2
    elif operator == '/':
        if number_2 == 0:
            print("Can't divison by zero!!")
            continue
        else:
            result = number_1 / number_2
    else:
        print("Please enter + , - , * or /")
        continue

    print(f"Result : {number_1} {operator} {number_2} = {result}")

    user_choice = input("Do you to continue [Y/N]: ")
    if user_choice.lower() == 'y':
        main_loop = True
    elif user_choice.lower() == 'n':
        main_loop = False
        print("Thank you.")

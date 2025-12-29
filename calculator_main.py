import calculator_utils

print("CALCULATOR")
operator = ['+', '-', '*', '/', '**', '%']
last_result = None
while True:
    try:
        if last_result is None:
            number_1 = calculator_utils.get_number("Enter 1st number: ")
        else:
            number_1 = last_result
            print(f"1st number : {number_1}")
        number_2 = calculator_utils.get_number("Enter 2nd number: ")
    except ValueError:
        print("Please enter number.")
        continue
    operator_input = calculator_utils.get_operation(
        "Enter the operator[+ ,- ,* ,/ ,% ,**]: ")

    if operator_input in operator:
        if operator_input in ('/', '%') and number_2 == 0:
            print("Can't divison by zero!!!")
            continue
        else:
            result = calculator_utils.calculate(
                number_1, number_2, operator_input)
    else:
        print("Please enter + , - , * , ** , '%' or /")
        continue

    print(
        f"Result : {number_1} {operator_input} {number_2} = {round(result, 2)}")

    user_choice = input("Do you to continue [Y/N]: ")
    if user_choice.lower() == 'y':
        use_last_result = input(
            "Do you want to use the previous result? [Y/N]: ")
        if use_last_result.lower() == 'y':
            last_result = round(result, 2)
        continue
    elif user_choice.lower() == 'n':
        print("Thank you.")
        break

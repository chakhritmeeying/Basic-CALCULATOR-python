import math


def calculate(number_1, number_2, operator):
    if operator == '+':
        return number_1 + number_2
    elif operator == '-':
        return number_1 - number_2
    elif operator == '*':
        return number_1 * number_2
    elif operator == '/':
        return number_1 / number_2
    elif operator == '**':
        return math.pow(number_1, number_2)
    elif operator == '%':
        return number_1 % number_2


def get_number(prompt):
    return float(input(prompt))


def get_operation(prompt):
    return input(prompt)

from random import randint, choice


GAME_RULE = 'What is the result of the expression?'
MIN_NUMBER = 0
MAX_NUMBER = 99
OPERATORS = ('*', '-', '+')


def get_question_and_answer():
    operator = choice(OPERATORS)
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = calculate(first_number, second_number, operator)
    question = f'{first_number} {operator} {second_number}'
    return question, correct_answer


def calculate(first_number, second_number, operator):
    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number
    return result

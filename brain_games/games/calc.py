from random import randint, choice


GAME_RULE = 'What is the result of the expression?'
MIN_NUMBER = 0
MAX_NUMBER = 99
OPERATORS = ('*', '-', '+')


def get_question_and_answer():
    random_operator = choice(OPERATORS)
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)
    if random_operator == '+':
        correct_answer = first_number + second_number
    elif random_operator == '-':
        correct_answer = first_number - second_number
    elif random_operator == '*':
        correct_answer = first_number * second_number
    question = f'{first_number} {random_operator} {second_number}'
    return question, correct_answer

from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 0
MAX_NUMBER = 99


def get_question_and_answer():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = number
    return question, correct_answer


def is_even(num):
    return num % 2 == 0

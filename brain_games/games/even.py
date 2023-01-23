from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 0
MAX_NUMBER = 99


def get_question_and_answer():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = is_even(number)
    question = number
    return question, correct_answer


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    get_question_and_answer()

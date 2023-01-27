from random import randint
from math import gcd


GAME_RULE = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 0
MAX_NUMBER = 99


def get_question_and_answer():
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = gcd(first_number, second_number)
    question = f'{first_number} {second_number}'
    return question, correct_answer

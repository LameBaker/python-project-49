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


'''def gcd(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number >= second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    result = first_number + second_number
    return result'''


def main():
    get_question_and_answer()

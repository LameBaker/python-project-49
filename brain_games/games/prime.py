from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 0
MAX_NUMBER = 99


def get_question_and_answer():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = is_prime(number)
    question = number
    return question, correct_answer


def is_prime(number):
    if number < 2:
        return 'no'
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def main():
    get_question_and_answer()

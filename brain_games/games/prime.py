from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 0
MAX_NUMBER = 99


def get_question_and_answer():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = number
    return question, correct_answer


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

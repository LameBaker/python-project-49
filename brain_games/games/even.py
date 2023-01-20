from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def engine():
    number = randint(0, 100)
    right_answer = is_even(number)
    question = number
    return question, right_answer


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'

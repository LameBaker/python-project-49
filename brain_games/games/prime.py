from random import randint


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def engine():
    number = randint(0, 100)
    right_answer = is_prime(number)
    question = number
    return question, right_answer


def is_prime(number):
    if number < 2:
        return 'no'
    else:
        for i in range(2, number // 2):
            if number % i == 0 or number < 2:
                return 'no'
    return 'yes'

from random import randint


GAME_RULES = 'Find the greatest common divisor of given numbers.'


def engine():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    right_answer = gcd(first_number, second_number)
    question = f'{first_number} {second_number}'
    return question, right_answer


def gcd(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number >= second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    result = first_number + second_number
    return result

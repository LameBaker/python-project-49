from random import randint


GAME_RULE = 'What number is missing in the progression?'
MIN_NUMBER = 0
MAX_NUMBER = 99
MIN_STEP = 1
MAX_STEP = 10
MIN_LENGTH = 5
MAX_LENGTH = 20


def get_question_and_answer():
    step = randint(MIN_STEP, MAX_STEP)
    length_progression = randint(MIN_LENGTH, MAX_LENGTH)
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer, question = \
        create_progression_and_secret(first_number, length_progression, step)
    return question, correct_answer


def create_progression_and_secret(first_number, length_progression, step):
    numbers = [first_number]
    for i in range(1, length_progression):
        numbers.append(numbers[-1] + step)
    secret_index = randint(0, length_progression - 1)
    secret_number = numbers[secret_index]
    progression_str = " ".join(map(str, numbers))
    progression = progression_str.replace(str(secret_number), '..')
    return secret_number, progression

from random import randint


GAME_RULES = 'What number is missing in the progression?'


def engine():
    step = randint(1, 10)
    length_progression = randint(5, 20)
    first_number = randint(0, 100)
    progressions = [first_number]
    for i in range(1, length_progression):
        progressions.append(progressions[-1] + step)
    secret_index = randint(0, length_progression - 1)
    right_answer = progressions[secret_index]
    progressions_str = " ".join(map(str, progressions))
    question = progressions_str.replace(str(right_answer), '..')
    return question, right_answer

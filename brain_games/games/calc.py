from random import randint, choice


GAME_RULES = 'What is the result of the expression?'


def engine():
    operators = ('*', '-', '+')
    random_operator = choice(operators)
    first_operand = randint(1, 99)
    second_operand = randint(1, 99)
    operators = ('+', '-', '*')
    random_operator = choice(operators)
    if random_operator == '+':
        right_answer = first_operand + second_operand
    elif random_operator == '-':
        right_answer = first_operand - second_operand
    else:
        right_answer = first_operand * second_operand
    question = f'{first_operand} {random_operator} {second_operand}'
    return question, right_answer


def main():
    engine()


if __name__ == '__main__':
    main()

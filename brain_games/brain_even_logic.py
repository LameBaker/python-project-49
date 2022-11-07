"""Brain_Even game implementation"""


from random import randint
from brain_games.cli import user_name


def brain_even_engine():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        num = randint(1, 99)
        right_answer = is_even(num)
        print(f'Question: {num}')
        user_answer = input('Your answer: ')
        if right_answer == user_answer:
            print('Correct!')
            i += 1
            continue
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    brain_even_engine()


if __name__ == '__main__':
    main()

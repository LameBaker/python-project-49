import prompt


def start_game(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.GAME_RULES)
    i = 0
    while i < 3:
        question, right_answer = game.engine()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if str(right_answer) == user_answer:
            print('Correct!')
            i += 1
            continue
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{right_answer}'.\n"
                f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
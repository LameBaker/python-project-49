import prompt


COUNT_ROUND = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.GAME_RULE)
    i = 0
    while i < COUNT_ROUND:
        question, correct_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if str(correct_answer) == user_answer:
            print('Correct!')
            i += 1
            continue
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')

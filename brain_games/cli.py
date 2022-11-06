"""User interaction script"""


import prompt

def welcome_user(name=str):
    """Print welcome message with name request"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def main():
    welcome_user()


if __name__ == '__main__':
    main()
"""User interaction script"""


import prompt


def welcome_user():
    """Print welcome message with name request"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


user_name = welcome_user()


def main():
    welcome_user()


if __name__ == '__main__':
    main()

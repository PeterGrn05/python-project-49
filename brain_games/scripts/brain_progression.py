from brain_games.cli import welcome_user
from ..games.progression_game import progression_game


def main():
    print('Welcome to the Brain Games!')
    n = welcome_user()
    if progression_game(n):
        win(n)


def win(arg):
    return print(f'Congratulations, {arg}!')


if __name__ == '__main__':
    main()
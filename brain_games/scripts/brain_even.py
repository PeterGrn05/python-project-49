from brain_games.cli import welcome_user
from ..games.even_game import even_game


def main():
    print('Welcome to the Brain Games!')
    n = welcome_user()
    if even_game(n) == 1:
        win(n)


def win(arg):
    return print(f'Congratulations, {arg}!')


if __name__ == '__main__':
    main()
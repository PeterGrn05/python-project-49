from brain_games.cli import welcome_user
from ..games.gcd_game import gcd_game


def main():
    print('Welcome to the Brain Games!')
    n = welcome_user()
    if gcd_game(n) == 1:
        win(n)


def win(arg):
    return print(f'Congratulations, {arg}!')


if __name__ == '__main__':
    main()
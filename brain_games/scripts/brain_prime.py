from brain_games.cli import welcome_user
from ..games.prime_game import prime_game
from random import randint


def main():
    print('Welcome to the Brain Games!')
    n = welcome_user()
    if prime_game(n) == 1:
        win(n)


def win(arg):
    return print(f'Congratulations, {arg}!')


if __name__ == '__main__':
    main()
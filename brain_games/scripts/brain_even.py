#!/usr/bin/env python3

from brain_games.cli import welcome_user
from random import randint

def main():
    print('Welcome to the Brain Games!')
    n = welcome_user()
    if even_game(n) == 1:
        win(n)

def even_game(arg):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = randint(0, 100)
        correct = 'yes' if number % 2 == 0 else 'no'
        print(f'Question: {number}')
        answer = input('Your answer: ')
        if answer == correct:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {arg}!")
            return False
    return True

def win(arg):
    return print(f'Congratulations, {arg}!')

if __name__ == '__main__':
    main()
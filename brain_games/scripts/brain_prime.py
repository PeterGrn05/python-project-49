#!/usr/bin/env python3

from brain_games.cli import welcome_user
from random import randint

def main():
    print('Welcome to the Brain Games!')
    n = welcome_user()
    if prime_game(n) == 1:
        win(n)

def is_prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_game(arg):
    print('Answer "yes" if the number is prime. Otherwise answer "no".')
    for _ in range(3):
        number = randint(0, 50)
        print(f'Question: {number}')
        correct = 'yes' if is_prime_number(number) else 'no'
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
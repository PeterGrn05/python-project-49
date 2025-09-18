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
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        number = randint(0, 50)
        print(f'Question: {number}')
        right = 'yes' if is_prime_number(number) else 'no'
        id = input('Your answer: ')
        if id == right:
            print('Correct!')
        else:
            print(f"'{id}' is wrong answer ;(. Correct answer was '{right}'.")
            print(f"Let's try again, {arg}!")
            return False
    return True


def win(arg):
    return print(f'Congratulations, {arg}!')


if __name__ == '__main__':
    main()
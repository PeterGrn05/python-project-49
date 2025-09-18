from brain_games.cli import welcome_user
from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    if gcd_game(name):
        print(f'Congratulations, {name}!')


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_game(name):
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        ch1, ch2 = randint(1, 100), randint(1, 100)
        right = gcd(ch1, ch2)
        print(f'Question: {ch1} {ch2}')
        id = input('Your answer: ').strip()

        if id == str(right):
            print('Correct!')
        else:
            print(f"'{id}' is wrong answer ;(. Correct answer was '{right}'.")
            print(f"Let's try again, {name}!")
            return False
    return True


if __name__ == '__main__':
    main()
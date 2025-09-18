from brain_games.cli import welcome_user
from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    if progression_game(name):
        print(f'Congratulations, {name}!')


def progression_game(name):
    print('What number is missing in the progression?')
    for _ in range(3):
        ch1, ch2, sh = randint(0, 10), randint(50, 60), randint(5, 10)
        numbers = list(range(ch1, ch2, sh))
        idx = randint(0, len(numbers) - 1)
        right = numbers[idx]
        numbers[idx] = '..'

        print('Question:', *numbers)
        id = input('Your answer: ')
        if id.strip() == str(right):
            print('Correct!')
        else:
            print(f"'{id}' is wrong answer ;(. Correct answer was '{right}'.")
            print(f"Let's try again, {name}!")
            return False
    return True


if __name__ == '__main__':
    main()
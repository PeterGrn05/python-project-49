from brain_games.cli import welcome_user
from random import randint, choice


def main():
    print('Welcome to the Brain Games!')
    n = welcome_user()
    if calc_game(n) == 1:
        win(n)


def calc_game(name):
    print('What is the result of the expression?')
    for _ in range(3):
        ch1, ch2 = randint(0, 100), randint(0, 100)
        op = choice('+-*')
        question = f"{ch1} {op} {ch2}"
        right = eval(question)
        print(f'Question: {question}')
        id = input('Your answer: ').strip()

        if id == str(right):
            print('Correct!')
        else:
            print(f"'{id}' is wrong answer ;(. Correct answer was '{right}'.")
            print(f"Let's try again, {name}!")
            return False
    return True


def win(arg):
    return print(f'Congratulations, {arg}!')


if __name__ == '__main__':
    main()
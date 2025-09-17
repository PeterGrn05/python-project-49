from brain_games.cli import welcome_user
from random import randint, choice

def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    if calc_game(name):
        print(f'Congratulations, {name}!')

def calc_game(name):
    print('What is the result of the expression?')
    for _ in range(3):
        ch1, ch2 = randint(0, 100), randint(0, 100)
        op = choice('+-*')
        question = f"{ch1} {op} {ch2}"
        correct = eval(question)
        print(f'Question: {question}')
        answer = input('Your answer: ').strip()

        if answer == str(correct):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return False
    return True

if __name__ == '__main__':
    main()
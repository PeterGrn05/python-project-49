from random import randint


def even_game(arg):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = randint(0, 100)
        right = 'yes' if number % 2 == 0 else 'no'
        print(f'Question: {number}')
        id = input('Your answer: ')
        if id == right:
            print('Correct!')
        else:
            print(f"'{id}' is wrong answer ;(. Correct answer was '{right}'.")
            print(f"Let's try again, {arg}!")
            return False
    return True
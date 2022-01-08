import random

num = ((random.random() * 90) // 10 ) + 1
chances = 5

while chances > 0:
    guess = float(input("Guess a number: "))
    if guess > num:
        print(f'Your guess was too big. Guess a number smaller than {guess}')
        chances -= 1
    elif guess < num:
        print(f'Your guess was too small. Guess a number bigger than {guess}')
        chances -= 1
    else:
        print(f'You were right. The number was {num}')
        chances = -1

if chances == 0:
    print(f'You failed. The number was {num}')
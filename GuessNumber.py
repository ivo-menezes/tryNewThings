# guess number 6 game with limit number of tries

guess = 0
tries = 0

while guess != 6 and tries < 3:
    guess = int(input("Guess the number: "))
    tries += 1
    if guess == 6:
        print('You got it!')
    elif tries == 3:
        print('You run out of tries!')
from random import randint

def user_input():
    return int(input('Enter a number between 1 and 100: '))

# method use to guest the user input
def guessing_number():
    # below use to get the random input from the machine
    machine_guess = randint(1, 100)
    counter = 1
    while True:
        # get the user input
        user_guess = user_input()
        if user_guess == machine_guess:
            print(f'Congratulations! You got it in {counter} guesses.')
            break
        elif user_guess > machine_guess:
            print(f'Too high. Try again: {user_guess}.')
        elif user_guess < machine_guess:
            print(f'Too low. Try again: {user_guess}.')
        counter += 1

if __name__ == '__main__':
    guessing_number()
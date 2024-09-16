# method use to test if statement
def if_statement():
    x = int(input("Please enter a number: "))
    # process use to get the int number
    if x < 0:
        x = 0
        # print its negative value
        print('Negative change to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('Multiple')

# method use to test for statement
def for_statement():
    words = ['cat', 'window', 'defenestrate']
    for word in words:
        print(word, len(word))

# match example
def http_error(status):
    match status:
        case 400:
            return 'Bad Request'
        case 404:
            return 'Not Found'
        case 500:
            return 'Internal Server Error'
        case 200 | 201 | 300:
            return 'Ok'
        case _:
            return 'Something went wrong'

# ask ok
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in ('y', 'ye', 'yes'):
            return True
        elif reply in ('n', 'no', 'no'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user input')
        print(reminder)
# positional arguments fun
def add(a, b):
    return a+b

# keyword arguments
def greet(name, message):
    print(f"{message}, {name}")

# default arguments
def greet1(name, message='Hello'):
    print(f"{message}, {name}")

# variable-length arguments
def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def handle_exception():
    try:
        x = int(input('Please enter a null value : '))
        print(f'Value :- {x}')
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# main function
if __name__ == '__main__':
    handle_exception()
    # print(sum_all(1,2,3,4,5))
    # print_info(apple="apple", orange="orange", banana="banana")
    # print(add(12, 234))
    # greet('nabeel', 'Ahmed')
    # greet(name='nabeel', message='Ahmed!')
    # greet1('Ahmed', 'sdaf')
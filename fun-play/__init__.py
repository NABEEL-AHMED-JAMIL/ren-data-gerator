# fun function use to add 1 argument
def fun0(name):
    return f'Name of user is :- {name}'

# fun1 function use to add the name and message
#  is optional bz its default value there
def fun1(name, message='H1'):
    return f'{message} & {name}'

# fun2 function have 2 parameters
def fun2(name='Nabeel', message='H2'):
    return f'{name} & {message}'

# main entry point to run the application
if __name__ == '__main__':
    # fun0
    print(fun0(name='Nabeel ahmed'))
    # fun1
    # print(fun1(''))
    # print(fun1('Nabeel', 'Pakistan'))
    # fun2
    # print(fun2())
    # print(fun2('Nabeel'))
    # print(fun2('Nabeel', 'Pakistan'))
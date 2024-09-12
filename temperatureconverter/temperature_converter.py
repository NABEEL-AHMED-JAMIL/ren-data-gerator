# Method use to convert Fahrenheit to Celsius
# Formulate :-  Tc=(5/9)*(Tf-32)
def to_celsius(tf = 0):
    tc = (5 / 9) * (tf - 32)
    return tc

# Method use to convert Celsius to Fahrenheit
# Formulate :- Tf=(9/5)*Tc+32
def to_fahrenheit(tc = 0):
    tf = (9 / 5) * tc + 32
    return tf

if __name__ == '__main__':
    print('Temperature converter')
    while True:
        try:
            temperature = int(input('Enter a temperature :- '))
            convertType = str(input('Convert to (F) Fahrenheit or (C) Celsius ? '))
            if convertType == 'F':
                print(f'Fahrenheit {to_fahrenheit(temperature)}')
            elif convertType == 'C':
                print(f'Celsius {to_celsius(temperature)}')
            else:
                print('Proces Exist No Convert Type Found.')
                exit(0)
        except ValueError:
            print('Please enter a number.')
# define a class
class Person:

    def __init__(self, name, age):
        self.name = name # Attribute
        self.age = age  # Attribute

    def greet(self): # Method
        return f"Hello, my name is {self.name} and I am {self.age} year old."


if __name__ == '__main__':
    person = Person("Nabeel Ahmed", 31)
    print(person.greet())
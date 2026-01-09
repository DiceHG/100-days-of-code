def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

num1 = float(input('Type the first number: '))
print('Type the desired operation')
for symbol in operations:
    print(symbol)
operation = input()
num2 = float(input('Type the second number: '))

print(operations[operation](num1, num2))
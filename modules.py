# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules
# File: main.py
import calculator
# File: calculator.py
import calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


a = 10
b = 5

print(calculator.add(a, b))
print(calculator.subtract(a, b))
print(calculator.multiply(a, b))
print(calculator.divide(a, b))


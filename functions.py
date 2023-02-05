# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print("The sum of 5 and 7 is:", result)



# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
square = lambda x: x * x

print(square(5))

sum = lambda x, y: x + y

print(sum(3, 4))


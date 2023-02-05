# If/ Else conditions are used to decide to do something based on something being true or false
num = 5

if num > 0:
    print(f"{num} is positive.")
else:
    print(f"{num} is non-positive.")

# In this example, num is assigned the value 5,and the if statement checks whether num is greater than 0
# Since it is, the code inside the if block is executed, and the output is 5 is positive.

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
num1 = 5
num2 = 10

if num1 < num2:
    print(f"{num1} is less than {num2}.")
else:
    print(f"{num1} is greater than or equal to {num2}.")



# Logical operators (and, or, not) - Used to combine conditional statements
age = 25
is_student = False

if age >= 18 and not is_student:
    print("Eligible for voting.")
else:
    print("Not eligible for voting.")




# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

a = [1, 2, 3]
b = [1, 2, 3]
c = a

if a is not b:
    print("a and b do not refer to the same object.")
else:
    print("a and b refer to the same object.")

if a is not c:
    print("a and c do not refer to the same object.")
else:
    print("a and c refer to the same object.")


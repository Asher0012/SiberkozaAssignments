# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruits = ['apple', 'banana', 'cherry']

# Using a for loop
for fruit in fruits:
    print(fruit)

# Using a while loop
count = 0

while count < len(fruits):
    print(fruits[count])
    count += 1


fruits = ['apple', 'banana', 'cherry', 'orange', 'grape']

for i, fruit in enumerate(fruits):
    print(f"{i+1}. I like to eat {fruit}.")

# While loops execute a set of statements as long as a condition is true.

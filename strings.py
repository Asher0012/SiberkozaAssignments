# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
# Define a string
my_string = "Hello, World!"

# Print the length of the string
print("The length of the string is:", len(my_string))

# Print the first character of the string
print("The first character of the string is:", my_string[0])

# Print a slice of the string
print("A slice of the string is:", my_string[7:12])

# Concatenate two strings
greeting = "Hello"
name = "arinzechukwu"
complete_greeting = greeting + ", " + name + "!"
print("The complete greeting is:", complete_greeting)

# Repeat a string
repeated_greeting = greeting * 3
print("The repeated greeting is:", repeated_greeting)

# Check if a string is contained in another string
is_hello_in_greeting = "Hello" in repeated_greeting
print("Is 'Hello' in the repeated greeting?", is_hello_in_greeting)

# Convert a string to uppercase
uppercase_greeting = greeting.upper()
print("The uppercase greeting is:", uppercase_greeting)

# Convert a string to lowercase
lowercase_greeting = greeting.lower()
print("The lowercase greeting is:", lowercase_greeting)


# String Formatting

# String Methods

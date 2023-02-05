# Python has functions for creating, reading, updating, and deleting files.

# Open a file for writing
file = open("example.txt", "w")

# Write some text to the file
file.write("Hello, World!")

# Close the file
file.close()

# Open the file for reading
file = open("example.txt", "r")

# Read and print the contents of the file
print("The contents of the file are:")
print(file.read())

# Close the file
file.close()

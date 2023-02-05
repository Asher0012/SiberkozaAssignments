# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Declare and initialize a dictionary
person = {'name': 'arinzechukwu nmaele', 'age': 24, 'gender': 'male'}

# Print the entire dictionary
print("The person's details are:", person)

# Access and print a specific value from the dictionary
print("The person's name is:", person['name'])

# Update a value in the dictionary
person['age'] = 35

# Print the updated dictionary
print("The updated person's details are:", person)

# Add a new key-value pair to the dictionary
person['address'] = '40 cankaya St.'

# Print the updated dictionary
print("The updated person's details are:", person)

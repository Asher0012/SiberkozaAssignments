# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

# A sample Python dictionary
person = {
    "first_name": "arinzechukwu",
    "last_name": "nmaele",
    "age": 24,
    "city": "ankara"
}

# Convert the dictionary to a JSON string
person_json = json.dumps(person)

# Print the JSON string
print(person_json)

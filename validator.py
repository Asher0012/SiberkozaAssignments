# Example of a custom module to be imported




        # Define a function to validate an email address
def validate_email(email):
    # Use a regular expression to check if the email address is valid
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

# Ask the user for an email address
email = input("Enter your email address: ")

# Validate the email address
if validate_email(email):
    print("The email address is valid.")
else:
    print("The email address is not valid.")


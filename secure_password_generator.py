"""
Filename: secure_password_generator.py
Author: Patrick Walsh
Date: 4/23/2021
Purpose: Randomly generates a secure password using both insecure and secure
randomization Python modules.
"""
import secrets
import random
import string

# sets variables for generating lowercase and uppercase letters, numbers, and special characters
LOWERCASE_LETTERS = string.ascii_letters[:26]
UPPERCASE_LETTERS = string.ascii_letters[26:]
NUMBERS = string.digits
SPECIAL_CHARACTERS = string.punctuation

# initialize password variable and set length
password = ""
length_password = 12

# iterate for the length of the password
for i in range(length_password):
    # get a random lowercase letter, uppercase letter, number, and special character
    characters = [secrets.choice(LOWERCASE_LETTERS), secrets.choice(UPPERCASE_LETTERS), secrets.choice(NUMBERS),
                  secrets.choice(SPECIAL_CHARACTERS)]

    # randomly add one of the characters to the password string
    if len(characters) == 1:
        password += characters[0]
    else:
        # password += characters[random.randint(0, len(characters)-1)]  # not secure randomization module
        password += characters[secrets.randbelow(len(characters) - 1)]  # secure randomization module

print("Password:", password)

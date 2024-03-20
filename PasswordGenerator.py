import random
import string

def generatePassword(minLength, numbers = True, specialCharacters = True):
    letters = string.ascii_letters
    digits = string.digits
    specialChar = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if specialCharacters:
        characters += specialChar

    password = ""
    meetsCriteria = False
    hasNumber = False
    hasSpecialCharacters = False

    while not meetsCriteria or len(password) < minLength:
        newChar = random.choice(characters)
        password += newChar

        if newChar in digits:
            hasNumber = True
        elif newChar in specialChar:
            hasSpecialCharacters = True

        meetsCriteria = True
        if numbers:
            meetsCriteria = hasNumber
        if specialCharacters:
            meetsCriteria = meetsCriteria and hasSpecialCharacters

    return password

minLength = int(input("Enter the minimum length for the password: "))
hasNumbers = input("Do you want to have numbers in your password (y/n) ? ").lower() == "y"
hasSpecialCharacters = input("Do you want to have special characters in your password (y/n) ? ").lower() == "y"

password = generatePassword(minLength, hasNumbers, hasSpecialCharacters)
print("The generated password is:", password)
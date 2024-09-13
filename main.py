# This program is the starter code for the Cracking Caesar's Cipher Project. 
# Inspired by "Cracking Codes with Python: An Introduction to Building and Breaking Ciphers" by Al Sweigart
# License: BSD Licensed

import string

# Global variables
lettersLower = string.ascii_lowercase
lettersUpper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
possibleCharacters = lettersLower + lettersUpper + numbers + symbols

# Define the function called decrypt
def decrypt(initialPosition, key):
    shiftedPosition = initialPosition - key
    return shiftedPosition

# Define the function called wraparound
def wraparound(shiftedPosition):
    if shiftedPosition < 0:
        shiftedPosition += len(possibleCharacters)
    return shiftedPosition

# Run code

# Introduction
print("Welcome! This program will crack the Caesar cipher and reveal the original message.")
print(f"Your message can include the following characters: {possibleCharacters}\n")

# Receive user input
initialMessage = input("What is your encrypted message? ")
input("\nPress Enter to generate all possible key decryptions for your message.\n")

# Cycle through all possible keys
for key in range(len(possibleCharacters)):
    shiftedMessage = ""

    # Decrypt the message
    for character in initialMessage:
        if character in possibleCharacters:
            initialPosition = possibleCharacters.find(character)
            shiftedPosition = decrypt(initialPosition, key)
            shiftedPosition = wraparound(shiftedPosition)
            shiftedMessage += possibleCharacters[shiftedPosition]
        else:
            shiftedMessage += character

    # Print the shifted message
    print(f"Key #{key}: {shiftedMessage}")

# Closing message
print("\nScroll through the key possibilities above to find the readable plaintext message.")

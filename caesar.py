"""
Ciphering/Deciphering using Caesar's Method
Caesar's Cipher represents a type of symmetrical stream ciphering.
Key space is limited, ranging from 1 to the alphabet's length minus 2, making it susceptible to brute-force attacks within a range of 1 to 24.
In stream ciphering, both encryption and decryption are executed bit by bit.
Symmetric ciphering involves performing both encryption and decryption procedures utilizing a confidential key.

"""
import random

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def caesar_encrypt(plain_text, shift):  # Encryption function
    if not (isinstance(shift, int) and shift > 0):
        return "Invalid shift value. Please provide a positive integer."

    plain_text = plain_text.lower()
    encrypted_text = ''

    for char in plain_text:
        if char in ALPHABET:
            encrypted_text += ALPHABET[(ALPHABET.index(char) + shift) % len(ALPHABET)]
        else:
            encrypted_text += char

    return encrypted_text
def caesar_decrypt(cipher_text, shift):  # Decryption function
    if not (isinstance(shift, int) and shift > 0):
        return "Invalid shift value. Please provide a positive integer."

    cipher_text = cipher_text.lower()
    decrypted_text = ''

    for char in cipher_text:
        if char in ALPHABET:
            decrypted_text += ALPHABET[(ALPHABET.index(char) - shift) % len(ALPHABET)]
        else:
            decrypted_text += char

    return decrypted_text

def generate_random_key():
    return random.randint(1, len(ALPHABET) - 1)

   # User input for plaintext and key
user_plaintext = input("Enter the plaintext: ")
user_key = int(input("Enter the key (a positive integer): "))

# Encrypt and display
encrypted_message = caesar_encrypt(user_plaintext, user_key)
print(f"Encrypted: {encrypted_message}")

# Decrypt and display
decrypted_message = caesar_decrypt(encrypted_message, user_key)
print(f"Decrypted: {decrypted_message}")

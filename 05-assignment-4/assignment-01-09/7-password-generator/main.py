import random

print("Welcome to your password generator!")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?/"

number = int(input("How many passwords do you want to generate? "))

length = int(input("How long do you want your passwords to be? "))

print("\nHere are your passwords:")
for password in range(number):
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    print(password)
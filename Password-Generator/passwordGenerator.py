import random
import secrets
import string

uppercaseCharacters = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercaseCharacters = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
numbers = string.digits  # '0123456789'
symbols = string.punctuation  # '!@#$%^&*()...'


def generatePassword():
    password = []
    passwordLength = random.randint(8, 32)
    for i in range(passwordLength):
        password.append(secrets.choice(uppercaseCharacters + lowercaseCharacters + numbers + symbols))

    random.shuffle(password)
    return ''.join(password)

newPassword = generatePassword()
print(newPassword)
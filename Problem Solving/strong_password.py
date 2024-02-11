def minimumNumber(n, password):
    required_characters = 0
    # Check if the password is missing each character type
    if not any(char.isdigit() for char in password):
        required_characters += 1
    if not any(char.islower() for char in password):
        required_characters += 1
    if not any(char.isupper() for char in password):
        required_characters += 1
    if not any(char in "!@#$%^&*()-+" for char in password):
        required_characters += 1

    # Check if the password length is less than 6 and add the difference to required_characters
    if n < 6:
        required_characters = max(required_characters, 6 - n)

    return required_characters



if __name__ == '__main__':

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    print(answer)
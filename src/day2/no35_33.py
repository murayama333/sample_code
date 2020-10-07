def palindrome(str):
    return str[::-1] == str


messages = ["txt", "html", "level"]
for message in messages:
    print(message, palindrome(message))

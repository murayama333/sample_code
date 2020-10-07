def pad_left(str, length, mark=" "):
    str_length = len(str)
    result = ""
    for _ in range(length - str_length):
        result = result + mark
    return result + str


names = ["Andy", "Bob"]
for name in names:
    print(pad_left(name, 5))
    print(pad_left(name, 5, "*"))

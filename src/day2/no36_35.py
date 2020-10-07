def pad_right(str, length, mark=" "):
    str_length = len(str)
    result = ""
    for _ in range(length - str_length):
        result = result + mark
    return str + result


names = ["Andy", "Bob"]
for name in names:
    print(pad_right(name, 5))
    print(pad_right(name, 5, "*"))

def repeat(str, count=2):
    result = ""
    for _ in range(count):
        result = result + str
    return result


message = "Hello"
print(repeat(message))
print(repeat(message, 5))

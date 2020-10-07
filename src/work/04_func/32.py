def truncate(str, length=10):
    if len(str) > length:
        pad = "..."
        pad_length = len(pad)
        return str[:length - pad_length] + pad
    return str


messages = ["Hello", "Hello World", "This is a pen."]
for message in messages:
    print(truncate(message, 10))

def contains(lst, value):
    return value in lst


names = ["Andy", "Bob", "Carol"]
print(names)
print("Bob:", contains(names, "Bob"))
print("Dave:", contains(names, "Dave"))

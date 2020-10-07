names = ["Andy", "Betty", "Carol"]
for i, name in enumerate(names):
    if i != len(names) - 1:
        print(name, end=",")
    else:
        print(name)

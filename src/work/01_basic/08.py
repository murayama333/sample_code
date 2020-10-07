rows = 9
columns = 9
symbol1 = "*"
symbol2 = " "

for i in range(rows):
    for j in range(columns):
        if j % 2 == 0:
            print(symbol1, end="")
        else:
            print(symbol2, end="")
    print()



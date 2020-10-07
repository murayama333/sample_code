rows = 9
columns = 9
symbol1 = "*"
symbol2 = " "

mid_column = columns // 2
row_column = rows // 2
for i in range(rows):
    for j in range(columns):
        if i == j or rows - i - 1== j:
            print(symbol2, end="")
        else:
            print(symbol1, end="")
    print()

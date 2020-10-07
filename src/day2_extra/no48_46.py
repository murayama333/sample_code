def print_space_board(rows=5, columns=5, symbol="*"):
    for i in range(rows):
        for j in range(columns):
            if i == 0 or j == 0 or i == rows - 1 or j == columns - 1:
                print(symbol, end="")
            else:
                print(" ", end="")
        print()

print_space_board()
print_space_board(rows=3, columns=9)
print_space_board(rows=6, columns=4 ,symbol="=")

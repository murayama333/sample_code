def print_board(rows=5, columns=5, symbol="*"):
    for i in range(rows):
        for j in range(columns):
            print(symbol, end="")
        print()

print_board()
print_board(rows=3, columns=9)
print_board(rows=6, columns=4 ,symbol="=")

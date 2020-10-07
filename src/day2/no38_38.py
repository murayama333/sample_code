def flat_list(td_list):
    return [element for lst in td_list for element in lst]


names = [["Andy", "Bob", "Carol"], ["Alice", "Betty", "Charlie"]]
print(flat_list(names))

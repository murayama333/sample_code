def pair_list(list1, list2):
    return [(e1, e2) for e1, e2 in zip(list1, list2)]


names1 = ["Andy", "Bob", "Carol"]
names2 = ["Alice", "Betty", "Charlie"]
print(pair_list(names1, names2))

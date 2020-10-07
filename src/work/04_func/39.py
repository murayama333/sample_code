def unique_list(lst):
    return sorted(list(set(lst)))

names = ["Andy", "Bob", "Carol", "Bob"]
print(unique_list(names))
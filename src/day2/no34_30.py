students = {"A-class": ["Alice", "Bob"],
            "B-class": ["Andy", "Bob", "Carol"],
            "C-class": ["Carol", "Daniel", "Ellen"]}

name_set = set()
for key, value in students.items():
    for name in value:
        name_set.add(name)
print(sorted(name_set))

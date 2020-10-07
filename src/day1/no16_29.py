students = {"A-class": ["Alice", "Bob"],
            "B-class": ["Andy", "Bob", "Carol"],
            "C-class": ["Carol", "Daniel", "Ellen"]}

for key, value in students.items():
    print(f"{key}:", len(value))

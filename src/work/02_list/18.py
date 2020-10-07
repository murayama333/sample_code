names_list = [["Ellen", "Betty", "Diana"],
              ["Fox", "Helen", "Andy"],
              ["Ian", "Glen", "Carol"]]

for names in names_list:
    for i, name in enumerate(names):
        if i != len(names) - 1:
            print(name, end=",")
        else:
            print(name)


names_list = [["Ellen", "Betty", "Diana"],
              ["Fox", "Helen", "Andy"],
              ["Ian", "Glen", "Carol"]]
end_with = "n"

for names in names_list:
    for name in names:
        if name[len(name) - 1] == end_with:
            print(name)

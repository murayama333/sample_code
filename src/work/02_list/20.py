names_list = [["Ellen", "Betty", "Diana"],
              ["Fox", "Helen", "Andy"],
              ["Ian", "Glen", "Carol"]]

flat_name_list = []
for names in names_list:
    for name in names:
        flat_name_list.append(name)

for name in sorted(flat_name_list):
    print(name)

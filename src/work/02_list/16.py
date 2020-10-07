names_list = [["Ellen", "Betty", "Diana"],
              ["Fox", "Helen", "Andy"],
              ["Ian", "Glen", "Carol"]]

index = 1
for names in names_list:
    for name in names:
        print(f"{index}:{name}")
        index = index + 1

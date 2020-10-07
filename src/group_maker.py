import random

group_count = int(input("Group Count: "))
shuffle = int(input("Shuffle (0: False, 1:True): "))
sort = int(input("Sort (0: False, 1:True): "))
print_mode = int(input("Print Mode (0: noraml, 1:table): "))

names = ["Alice", "Alex", "Andy", "Abel", "Albert",
        "Betty", "Bob", "Bella", "Billie", "Benn",
        "Carol", "Connie", "Crysta", "Clara", "Cyndy",
        "Daniel", "David", "Denny", "Diana"]

member_count = len(names)
group_member_count = member_count // group_count
rest_member = member_count % group_count

print("Member Count:", member_count)
print("Group Member Count:", group_member_count)
print("Rest Member Count:", rest_member)

group_member_counts = []
for i in range(group_count):
    if rest_member > 0:
        group_member_counts.append(group_member_count + 1)
        rest_member = rest_member - 1
    else:
        group_member_counts.append(group_member_count)
print("Group Member Counts:", group_member_counts)

if shuffle == 1:
    random.shuffle(names)

group_members_list = []
offset = 0
for group_member_count in group_member_counts:
    group_members = []
    for name in names[offset:offset + group_member_count]:
        group_members.append(name)
    group_members_list.append(group_members)
    offset = offset + group_member_count

if print_mode == 1:
    name_max_length = max([len(name) for name in names])
    for group_members in group_members_list:
        print("|", end="")
        if sort == 1:
            group_members = sorted(group_members)
        for group_member in group_members:
            print(f"{group_member:{name_max_length}}", end="|")
        print()
else:
    for i, group_members in enumerate(group_members_list):
        print(f"Group{i + 1}", end=": ")
        if sort == 1:
            group_members = sorted(group_members)
        for group_member in group_members:
            print(group_member, end=" ")
        print()

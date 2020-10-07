names = ["Andy", "Bob", "Carol", "Daniel", "Ellen"]
except_names = ["Andy", "Carol"]

result = []
for name in names:
    if name not in (except_names):
        result.append(name)

print(result)

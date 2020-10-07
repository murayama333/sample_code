scores = {"Math": [90, 95, 100],
          "English": [80, 85, 90],
          "Science": [70, 75, 80]}

for key, value in scores.items():
    print(f"{key} Total:", sum(value))

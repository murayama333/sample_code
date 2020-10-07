scores = {"Math": [90, 95, 100],
          "English": [80, 85, 90],
          "Science": [70, 75, 80]}

score_list = []
for key, value in scores.items():
    for score in value:
        score_list.append(score)

print("Total Score:", sum(score_list))

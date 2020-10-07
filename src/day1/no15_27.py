scores = {"Andy": (80, 90, 90),
          "Betty": (75, 85, 95),
          "Carol": (90, 70, 90),
          "Dave": (90, 90, 80)}

name_score_dict = {key: sum(value) for key, value in scores.items()}

high_score = 0
for name, score in name_score_dict.items():
    if high_score < score:
        high_score = score

for name, score in name_score_dict.items():
    if score == high_score:
        print(f"High Score {name}:", score)

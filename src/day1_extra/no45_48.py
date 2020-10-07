scores = [90, 95, 80, 85, 80, 95, 80, 90, 100]

score_dict = {}
for score in scores:
    count = 1
    if score in score_dict.keys():
        count = score_dict[score]
        count = count + 1
    score_dict[score] = count

max_score_count = max(score_dict.values())
for score, count in score_dict.items():
    if count == max_score_count:
        print("Mode:", score)

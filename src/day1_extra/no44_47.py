scores = [90, 95, 80, 85, 80, 95, 80, 90, 100]

score_count_dict = {}
for score in scores:
    count = 1
    if score in score_count_dict.keys():
        count = score_count_dict[score]
        count = count + 1
    score_count_dict[score] = count

for score, count in score_count_dict.items():
    print(f"{score:3}:", count)
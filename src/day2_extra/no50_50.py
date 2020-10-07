def mean_median_mode(scores):
    mean = sum(scores) // len(scores)
    mid = len(scores) // 2
    median = sorted(scores)[mid]

    score_dict = {}
    for score in scores:
        count = 1
        if score in score_dict.keys():
            count = score_dict[score]
            count = count + 1
        score_dict[score] = count
    mode = 0
    max_score_count = max(score_dict.values())
    for score, count in score_dict.items():
        if count == max_score_count:
            mode = score
            break
    return mean, median, mode


scores = [90, 95, 80, 85, 80, 95, 80, 90, 100]
mean, median, mode = mean_median_mode(scores)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

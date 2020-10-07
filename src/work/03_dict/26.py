names = ["Andy", "Betty", "Carol"]
scores = [80, 90, 100]
score_dict = {}
for name, score in zip(names, scores):
    score_dict[name] = score
print(score_dict)
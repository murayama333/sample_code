import json


class ScoreAnalyzer:
    def __init__(self, scores):
        self.scores = scores

    def print_scores(self):
        print("- scores -")
        for score in self.scores:
            print(f"{score['name']} {score['math']} {score['english']} {score['science']}")

    def print_total_score(self):
        print("- total scores -")
        total = 0
        for score in self.scores:
            total += score['math'] + score['english'] + score['science']
        print(total)

    def print_scores_by_subject(self, subject, with_name=False):
        print(f"- scores by {subject} -")
        for score in self.scores:
            if with_name: 
                print(score["name"], end=" ") 
            print(score[subject])
    
    def print_total_score_by_subject(self, subject):
        print(f"- total score by {subject} -")
        total = 0
        for score in self.scores:
            total += score[subject]
            
        print(total)

    def save(self, file_name):
        with open(file_name, "w") as f:
            json.dump(self.scores, f, indent=4)


if __name__ == "__main__":
    scores = [
        {"name": "Andy", "math": 70, "english": 90, "science": 80},
        {"name": "Betty", "math": 80, "english": 90, "science": 100},
        {"name": "Carol", "math": 40, "english": 90, "science": 90},
        {"name": "Daniel", "math": 80, "english": 100, "science": 40},
        {"name": "Ellen", "math": 90, "english": 70, "science": 90},
    ]
    score_analyzer = ScoreAnalyzer(scores)
    score_analyzer.save("score.json")

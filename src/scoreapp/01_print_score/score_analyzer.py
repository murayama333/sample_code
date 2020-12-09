import json


class ScoreAnalyzer:
    def __init__(self, scores):
        self.scores = scores

    def print_scores(self):
        print("- scores -")
        for score in self.scores:
            print(f"{score['name']} {score['math']} {score['english']} {score['science']}")


if __name__ == "__main__":
    scores = [
        {"name": "Andy", "math": 70, "english": 90, "science": 80},
        {"name": "Betty", "math": 80, "english": 90, "science": 100},
        {"name": "Carol", "math": 40, "english": 90, "science": 90},
        {"name": "Daniel", "math": 80, "english": 100, "science": 40},
        {"name": "Ellen", "math": 90, "english": 70, "science": 90},
    ]
    score_analyzer = ScoreAnalyzer(scores)
    score_analyzer.print_scores()

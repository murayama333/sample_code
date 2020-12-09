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

    @classmethod
    def load(cls, file_name):
        with open(file_name, "r") as f:
            scores = json.load(f)
            return ScoreAnalyzer(scores)

if __name__ == "__main__":
    score_analyzer = ScoreAnalyzer.load("score.json")
    score_analyzer.print_scores()

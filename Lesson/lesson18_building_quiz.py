# Building A Quiz
# This is the class
class Question:
    def __init__ (self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b)Orange\n\n",
    "What color are bananas?\n(a) Red/Green\n(b)Yellow\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
]

# This is excude
def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got", str(score), "out of", str(len(questions)))

run_quiz(questions)
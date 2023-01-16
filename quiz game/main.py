from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

QUESTION_BANK = []

for item in question_data:
    question = Question(item["question"], item["correct_answer"])
    QUESTION_BANK.append(question)

quiz_brain = QuizBrain(QUESTION_BANK)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz_brain.score}/{len(QUESTION_BANK)}")



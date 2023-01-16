from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

QUESTION_BANK = []

for item in question_data:
    question = Question(item["text"], item["answer"])
    QUESTION_BANK.append(question)

quiz_brain = QuizBrain(QUESTION_BANK)
quiz_brain.next_question()





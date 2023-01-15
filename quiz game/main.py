from question_model import Question
from data import question_data

QUESTION_BANK = []

for item in question_data:
    question = Question(item["text"], item["answer"])
    QUESTION_BANK.append(question)

print(QUESTION_BANK)

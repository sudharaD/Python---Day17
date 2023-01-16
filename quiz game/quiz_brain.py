class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your currant score is: {self.score}/{self.question_number+1}.\n")

    def next_question(self):
        answer = input(f"Q.{self.question_number+1}. {self.question_list[self.question_number].question} (True/"
                       f"False)?:  ")
        self.check_answer(answer, self.question_list[self.question_number].answer)
        self.question_number += 1






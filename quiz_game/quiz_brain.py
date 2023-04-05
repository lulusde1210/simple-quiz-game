class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        """check if there is still questions left"""
        return self.question_number < len(self.question_list)

    def ask_question(self):
        """prompt user to answer questions."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}:{current_question.text} (True/False):")
        self.check_answer(user_answer, current_question.answer)
        self.display_score()
        print("\n")

    def check_answer(self, user_answer, correct_answer):
        """check if the user's answer is correct or not"""
        if user_answer.capitalize() == correct_answer:
            self.score += 1
            print("You got it!")
        else:
            print("Sorry, that's wrong!")

        print(f"The correct answer is {correct_answer}!")

    def display_score(self):
        """display scores"""
        print(f"Your current score is {self.score}/{self.question_number}")

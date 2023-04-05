from quiz_game.question_model import Question
import random


class QuizManager:
    def __init__(self, question_data):
        self.question_data = question_data

    def choose_questions_from_data(self):
        """Chose 10 random questions from question data"""
        random_questions = []
        for _ in range(10):
            random_index = random.randrange(0, len(self.question_data))
            random_question = self.question_data[random_index]
            random_questions.append(random_question)
        return random_questions

    def create_question_bank(self):
        """Create a question bank from question data"""
        question_bank = []
        for question in self.choose_questions_from_data():
            text = question["question"]
            answer = question["correct_answer"]
            new_question = Question(text, answer)
            question_bank.append(new_question)
        return question_bank

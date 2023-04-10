from quiz_game.question_model import Question
import random


class QuizManager:
    def __init__(self, question_data):
        self.question_data = question_data

    def create_question_bank(self):
        """Create a question bank from question data"""
        question_bank = []
        for question in self.question_data:
            text = question["question"]
            answer = question["correct_answer"]
            new_question = Question(text, answer)
            question_bank.append(new_question)
        return question_bank

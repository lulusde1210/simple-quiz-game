from quiz_game.quiz_brain import QuizBrain
from quiz_game.quiz_manager import QuizManager
from data.data import question_data

quiz_manager = QuizManager(question_data)
question_bank = quiz_manager.create_question_bank()
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.ask_question()

print(
    f"You've completed the quiz! Your final score is {quiz_brain.score}/{len(question_bank)}")

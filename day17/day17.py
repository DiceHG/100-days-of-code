from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(question["question"], question["correct_answer"]) for question in question_data]
quiz = QuizBrain(question_bank)

while quiz.has_questions_left():
    quiz.next_question()

print("You have finished the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
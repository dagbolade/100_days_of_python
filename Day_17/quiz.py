from quiz_brain import QuizBrain
from question_model import Question
from data import question_data


question_bank = []

for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    # creating a new question object
    new_question = Question(q_text, q_answer)
    # adding the new question object to the question_bank list
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

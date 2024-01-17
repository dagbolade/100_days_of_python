from quiz_brain import QuizBrain
from question_model import Question
from data import question_data


question_bank = [] # creating an empty list to store the question objects

for question in question_data: # looping through the question_data list
    q_text = question["question"] # retrieving the question text from the question_data list
    q_answer = question["correct_answer"] # retrieving the question answer from the question_data list
    # creating a new question object
    new_question = Question(q_text, q_answer) # passing in the question text and the question answer as arguments
    # adding the new question object to the question_bank list
    question_bank.append(new_question) # appending the new question object to the question_bank list

quiz = QuizBrain(question_bank) # creating a new quiz object and passing in the question_bank list as an argument

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
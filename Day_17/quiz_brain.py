# creating a quiz_brain class


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # create a method to check if there are more questions
    def still_has_questions(self):
        # return true if there are more questions or false if there are no more questions
        return self.question_number < len(self.question_list)

    # create a method to ask for the next question
    def next_question(self):
        # retrieve item at current question number from a question list
        current_question = self.question_list[self.question_number]
        # increment the question number by 1
        self.question_number += 1
        # use the input function to show the question text and ask for the user's answer
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # check if the user's answer is correct
        self.check_answer(user_answer, current_question.answer)

    # create a method to check if the user's answer is correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")


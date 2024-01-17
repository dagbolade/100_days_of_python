# creating a quiz_brain class


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

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
        input(f"Q.{self.question_number}: {current_question.text} (True/False): ")

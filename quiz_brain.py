# Defining a class named QuizBrain to manage the quiz logic.
class QuizBrain:
    # Constructor method for initializing a QuizBrain object with a list of Question objects.
    def __init__(self, q_list):
        # Initializing the question number to 0 (starting point of the quiz).
        self.question_number = 0
        # Storing the list of Question objects in the 'question_list' attribute.
        self.question_list = q_list
        # Initializing the score to 0 (starting score of the quiz).
        self.score = 0

    # Method to check the user's answer against the correct answer.
    def check_answer(self, user_answer, correct_answer):
        # Comparing the user's answer to the correct answer, case-insensitively.
        if user_answer.lower() == correct_answer.lower():
            # Incrementing the score if the answer is correct.
            self.score += 1
            print("You got it right!")  # Printing a message for a correct answer.
        else:
            print("That's wrong")  # Printing a message for an incorrect answer.
        # Displaying the correct answer.
        print(f"The correct answer is {correct_answer}")
        # Displaying the current score and question number.
        print(f"The current score is {self.score}/{self.question_number}")
        print("\n")

    # Method to check if there are still questions remaining in the quiz.
    def still_has_questions(self):
        # Returns True if the current question number is less than the total number of questions.
        return self.question_number < len(self.question_list)

    # Method to display the next question and get the user's answer.
    def next_question(self):
        # Retrieving the current question based on the question number.
        current_question = self.question_list[self.question_number]
        # Incrementing the question number for the next call.
        self.question_number += 1
        # Prompting the user for their answer to the current question.
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        # Checking the user's answer.
        self.check_answer(user_answer, current_question.answer)

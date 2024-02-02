# Importing the question_data list from the data.py file.
from data import question_data
# Importing the Question class from the question_model.py file.
from question_model import Question
# Importing the QuizBrain class from the quiz_brain.py file.
from quiz_brain import QuizBrain

# Initialize an empty list to store Question objects.
question_bank = []
# Loop over each item in the question_data list.
for data in question_data:
    # Creating a Question object for each question in the dataset with its text and answer.
    q_data = Question(data["question"], data["correct_answer"])
    # Appending the created Question object to the question_bank list.
    question_bank.append(q_data)

# Creating a QuizBrain object with the question_bank list as its input.
quiz = QuizBrain(question_bank)

# Looping through the quiz as long as there are questions remaining.
while quiz.still_has_questions():
    # Calling the next_question method to display the next question and handle user input.
    quiz.next_question()
# Printing a message when the quiz is complete.
print("You've completed the quiz")
# Printing the final score of the user out of the total number of questions.
print(f"Your final score is {quiz.score}/{quiz.question_number}")

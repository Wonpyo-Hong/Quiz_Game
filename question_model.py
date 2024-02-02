# Defining a class named Question to encapsulate each quiz question.
class Question:
    # Constructor method for initializing a Question object with question text and its answer.
    def __init__(self, q_text, q_answer):
        # Storing the question text in the 'text' attribute.
        self.text = q_text
        # Storing the correct answer in the 'answer' attribute.
        self.answer = q_answer

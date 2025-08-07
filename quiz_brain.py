import html

class QuizBrain:

    def __init__(self, q_list):
        """
        Constructor for QuizBrain object.

        Args:
            q_list (list): A list of Question objects.

        Sets the question number to 0, the score to 0, the question list to the input list,
        and the current question to None.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """
        Checks if there are any questions left.

        Returns:
            bool: True if there are still questions left, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Presents the next question to the user and prompts for an answer.

        This method retrieves the next question from the question list, increments
        the question number, and then displays the question to the user. The user's
        answer is obtained via input and passed to the check_answer method for
        validation.

        Returns:
            None
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        self.check_answer(user_answer)

    def check_answer(self, user_answer):
        """
        Checks if the user's answer is correct.
        
        Args:
            user_answer (str): The user's answer to the current question.
        
        Returns:
            None
        """
        #check to make sure self.current_question is not None before accessing its answer attribute.
        if self.current_question is None:   
            print("No current question set.")
            return
        
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

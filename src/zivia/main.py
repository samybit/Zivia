from .question_model import Question
from .data import question_data
from .quiz_brain import QuizBrain
from .ui import QuizInterface

def main():
    # Create a bank of questions
    question_bank: list[Question] = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    # Create a QuizBrain object and a QuizInterface object
    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz) # type: ignore

    # End message and display the final score
    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")

if __name__ == "__main__":
    main()

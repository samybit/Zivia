import tkinter as tk
from quiz_brain import QuizBrain
from pathlib import Path

THEME_COLOR = "#B6BAB3"
QUESTION_COLOR = "#121015"
SCORE_COLOR = "#D71134"
CANVAS_COLOR = "#A8B082"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Window setup
        self.window = tk.Tk()
        self.window.title("Zivia")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Score label
        self.score_label = tk.Label(
            text="Score: 0",
            fg=SCORE_COLOR,
            bg=THEME_COLOR,
            font=("Arial", 20, "bold")
        )
        self.score_label.grid(row=0, column=1)

        # Canvas to display the question
        self.canvas = tk.Canvas(
            width=350,
            height=250,
            bg="white",
            highlightthickness=4,
            highlightbackground=SCORE_COLOR
        )
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=310,
            text="Question goes here",
            fill=QUESTION_COLOR,
            font=("Arial", 20, "bold")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        TRUE_IMAGE_PATH = Path(__file__).parent / "images/true.png"
        FALSE_IMAGE_PATH = Path(__file__).parent / "images/false.png"

        # Buttons for true and false
        self.true_image = tk.PhotoImage(file=TRUE_IMAGE_PATH)
        self.true_button = tk.Button(
            image=self.true_image,
            highlightthickness=0,
            bd=0,
            relief="flat",
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0)

        self.false_image = tk.PhotoImage(file=FALSE_IMAGE_PATH)
        self.false_button = tk.Button(
            image=self.false_image,
            highlightthickness=0,
            bd=0,
            relief="flat",
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self) -> None:
        self.canvas.config(bg=CANVAS_COLOR)

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}|10")
            q_text = self.quiz.next_question()
            
            # Dynamically adjust font size based on question length
            if len(q_text) > 120:
                font_size = 16
            else:
                font_size = 20
            
            # Update both the text and the font in the same call
            self.canvas.itemconfig(
                self.question_text,
                text=q_text,
                font=("Arial", font_size, "italic")
            )

        else:
            self.canvas.itemconfig(
                self.question_text,
                text="Quiz Ended.",
                font=("Arial", 20, "bold")
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self) -> None:
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self) -> None:
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool) -> None:
        if is_right:
            self.canvas.config(bg="#00FF00")
        else:
            self.canvas.config(bg="#FF0000")
        self.window.after(1000, self.get_next_question)

from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#000000"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Window setup
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Score label
        self.score_label = Label(text="Score: 0", fg="#FFD54F", bg=THEME_COLOR, font=("Luckiest Guy", 20, "bold"))
        self.score_label.grid(row=0, column=1)

        # Canvas to display the question
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question goes here",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons for true and false
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image, 
            highlightthickness=0, 
            bd=0, 
            relief="flat",
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            command=None)
        self.true_button.image = true_image  # prevents python garbage collection
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_image, 
            highlightthickness=0, 
            bd=0, 
            relief="flat",
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            command=None)
        self.false_button.image = false_image  # prevents python garbage collection
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """
        Fetches the next question from the quizbrain and updates the UI.
        """
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT=("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0, pady=20)

        self.canvas = Canvas(bg="white", height=250, width=300)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Question",
            fill=THEME_COLOR,
            font=FONT,
            width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, command=self.true_pressed)
        self.true_button.grid(column=0, row=2, pady=20)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, command=self.false_pressed)
        self.false_button.grid(column=1, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def change_bg(self, is_correct: bool):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

    def give_feedback(self, is_correct):
        # time.sleep # can't because we're using mainloop
        bg = "green" if is_correct else "red"
        self.canvas.config(bg=bg)
        self.window.after(1000, self.get_next_question)


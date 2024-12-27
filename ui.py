from idlelib.configdialog import font_sample_text
from tkinter import *
from quiz_brain import QuizBrain
from numpy.ma.extras import column_stack

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.canvas = Canvas(height=250,width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Hello",font=("Arial",20,"italic"),
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        self.correct_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=self.correct_image, highlightthickness=0,command=self.true_answer)
        self.correct_button.grid(row=2,column=0)

        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image,highlightthickness=0,command=self.false_answer)
        self.wrong_button.grid(row=2,column=1)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text="You've reached the end of the quiz.")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer(user_answer="true"))

    def false_answer(self):
        is_right = self.quiz.check_answer(user_answer="false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
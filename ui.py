from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

FONT = ("Arial", 20, "italic")

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.windows = Tk()
        self.windows.title("quizler ")
        self.windows.config(bg=THEME_COLOR, padx=20, pady=20)

        self.quiz = quiz_brain

        self.score = 0

        self.score_label = Label(text=f"score: {self.score}", fg="white",bg= THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="some question", fill=THEME_COLOR, font=FONT, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true = Button(image=true_image, highlightthickness=0, command=self.right)
        self.true.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false = Button(image=false_image, highlightthickness=0, command=self.wrong)
        self.false.grid(column=1, row=2)

        self.next_question()
        self.windows.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= "OUT OF QUESTIONS")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def right(self):
        ans = "true"
        self.check_answer(ans)


    def wrong(self):
        ans = "false"
        self.check_answer(ans)

    def check_answer(self, ans):
        if self.quiz.check_answer(ans):
            self.score += 1
            self.score_label.config(text=f"score: {self.score}")
            self.canvas.config(bg="green")
            self.windows.after(1000, self.next_question)

        else:
            self.canvas.config(bg="red")
            self.windows.after(1000,self.next_question)


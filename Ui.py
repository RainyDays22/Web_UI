#import turtle
from tkinter import *
# add widgets here
#root = tk.Tk()
#canvas = tk.Canvas(root)
#canvas.config(width=600, height=200)
#canvas.pack(side=tk.LEFT)
#screen = turtle.TurtleScreen(canvas)
#screen.bgcolor("cyan")

questions = {1:['question 1 title!', 'rats', 'cats', 'hats', 'mats'],
            2:['question 2 title!', 'option 1', 'option 2', 'option 3', 'option 4']}
print(questions[1][0],questions[1][1])

class Quiz:

    def __init__(self, win):
        self.frame = Frame(win)
        self.frame.pack()
        self.lbl = Label(self.frame, text = 'What W&M animal are you?')
        self.lbl.pack()
        self.enter_btn = Button(self.frame, text="Enter quiz", command=self.next_question)
        self.enter_btn.pack()
        self.answers = []

    def track_answers(self, text):
        self.answers.append(text)
    
    def question(self, title, option1, option2, option3, option4):
        self.title = Label(self.frame, text = title)
        self.title.pack()
        self.option1 = Button(self.frame, text = option1, command = self.track_answers('A'))
        self.option1.pack()
        self.option2 = Button(self.frame, text = option2, command = self.track_answers('B'))
        self.option2.pack()
        self.option3 = Button(self.frame, text = option3, command = self.track_answers('C'))
        self.option3.pack()
        self.option4 = Button(self.frame, text = option4, command = self.track_answers('D'))
        self.option4.pack()

    def next_question(self):
        for i in self.frame.winfo_children():
            i.destroy()
        self.question(questions[1][0], questions[1][1], questions[1][2], questions[1][3], questions[1][4])

    

#https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python

#https://stackoverflow.com/questions/44634947/how-to-set-a-turtle-to-a-turtle-screen/44639041#44639041

#root.mainloop()
window = Tk()
window.title('Quiz')
window.geometry('400x300')
quiz = Quiz(window)
#quiz.option1('this is a button!')
window.mainloop()
#print(quiz)

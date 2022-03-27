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

def add_A(self):
    self.answers.append('A')

def add_B(self):
    self.answers.append('B')

def add_C(self):
    self.answers.append('C')

def add_D(self):
    self.answers.append('D')

class Quiz:

    def __init__(self, win):
        self.frame = Frame(win)
        self.frame.pack()
        self.lbl = Label(self.frame, text = 'What W&M animal are you?')
        self.lbl.pack()
        self.enter_btn = Button(self.frame, text="Enter quiz", command=self.next_question)
        self.enter_btn.pack()
        self.answers = []
        self.counter = 1

    def question_counter(self):
        return self.counter

    def track_answers(self):
        return self.answers
    
    def question(self, title, option1, option2, option3, option4):
        self.title = Label(self.frame, text = title)
        self.title.pack()
        self.option1 = Button(self.frame, text = option1, command = add_A)
        self.option1.pack()
        self.option2 = Button(self.frame, text = option2, command = add_B)
        self.option2.pack()
        self.option3 = Button(self.frame, text = option3, command = add_C)
        self.option3.pack()
        self.option4 = Button(self.frame, text = option4, command = add_D)
        self.option4.pack()
        print('we are here')
        print(self.track_answers())
        self.next_question()

    def next_question(self):
        for i in self.frame.winfo_children():
            i.destroy()
        q = self.counter
        if self.counter < 2:
            self.question(questions[q][0], questions[q][1], questions[q][2], questions[q][3], questions[q][4])
            self.counter += 1
        else:
            pass #end result

    

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

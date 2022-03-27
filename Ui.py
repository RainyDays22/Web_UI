#import turtle
from tkinter import *
import sys
# add widgets here
#root = tk.Tk()
#canvas = tk.Canvas(root)
#canvas.config(width=600, height=200)
#canvas.pack(side=tk.LEFT)
#screen = turtle.TurtleScreen(canvas)
#screen.bgcolor("cyan")
import urllib.request
from PIL import ImageTk, Image


questions = {0:['question 1 title!', 'rats', 'cats', 'hats', 'mats'],
            1:['question 2 title!', 'option 1', 'option 2', 'option 3', 'option 4'],
            2:['question 3 title!', 'option 1', 'option 2', 'option 3', 'option 4']}


class Quiz:

    def __init__(self, win):
        self.frame = Frame(win)
        self.frame.pack()
        lbl = Label(self.frame, text = 'What W&M animal are you?')
        lbl.pack()
        enter_btn = Button(self.frame, text="Enter quiz", command=self.next_question)
        enter_btn.pack()
        self.answers = []
        self.counter = 0
        self.finish = win.attributes('-fullscreen', True)
        exit_btn = Button(self.frame, text="Exit Fullscreen", command=self.exit)
        exit_btn = exit_btn.pack(side=TOP, anchor=NW)
        
    def exit(self):
        sys.exit()
       

    def question_counter(self):
        return self.counter

    def track_answers(self):
        return self.answers

    def add_A(self):
        self.answers.append('A')

    def add_B(self):
        self.answers.append('B')

    def add_C(self):
        self.answers.append('C')

    def add_D(self):
        self.answers.append('D')
    
    def question(self, title, option1, option2, option3, option4):
        title = Label(self.frame, text = title)
        title.pack()
        option1 = Button(self.frame, text = option1, command = lambda:[self.add_A(), self.next_question()])
        option1.pack()
        option2 = Button(self.frame, text = option2, command = lambda:[self.add_B(), self.next_question()])
        option2.pack()
        option3 = Button(self.frame, text = option3, command = lambda:[self.add_C(), self.next_question()])
        option3.pack()
        option4 = Button(self.frame, text = option4, command = lambda:[self.add_D(), self.next_question()])
        option4.pack()
        print('we are here')
        print(self.track_answers())

    def evaluate(self):
        A_counter = 0
        B_counter = 0
        C_counter = 0
        D_counter = 0
        for i in self.answers:
            if i == 'A':
                A_counter += 1
            if i == 'B':
                B_counter += 1
            if i == 'C':
                C_counter += 1
            if i == 'D':
                D_counter += 1
        print(A_counter,'As',B_counter,'Bs',C_counter,'Cs',D_counter,'Ds')
        if A_counter > B_counter and A_counter > C_counter and A_counter > D_counter:
            return 'squirrel'
        elif B_counter > A_counter and B_counter > C_counter and B_counter > D_counter:
            return 'frog'
        elif C_counter > A_counter and C_counter > B_counter and C_counter > D_counter:
            return 'Swem therapy dog'
        elif D_counter > A_counter and D_counter > B_counter and D_counter > C_counter:
            return 'blue heron'

    def end(self):
        result = self.evaluate()
        title = Label(text = 'You are a ' + str(result) + '!')
        title.pack()
        if result == 'squirrel':
            urllib.request.urlretrieve('https://i.imgur.com/PEIFopL.jpg', 'squirrel.jpeg')
            squirrel_pic = Image.open('squirrel.jpeg')
            squirrel = ImageTk.PhotoImage(squirrel_pic)
            label = Label(image = squirrel)
            label.image = squirrel
            label.pack()
            desc = Label(text = 'add a description of u as squirrel here')
            desc.pack()
        if result == 'frog':
            urllib.request.urlretrieve('https://i.imgur.com/McbobUQ.jpeg', 'frog.jpeg')
            frog_pic = Image.open('frog.jpeg')
            frog = ImageTk.PhotoImage(frog_pic)
            label = Label(image = frog)
            label.image = frog
            label.pack()
            desc = Label(text = 'add a description of u as frog here')
            desc.pack()
        if result == 'Swem therapy dog':
            urllib.request.urlretrieve('https://events.wm.edu/images/event_uploads/sjgilliam_2018_10_04_14_43_59.jpg', 'dog.jpeg')
            dog_pic = Image.open('dog.jpeg')
            dog = ImageTk.PhotoImage(dog_pic)
            label = Label(image = dog)
            label.image = dog
            label.pack()
            desc = Label(text = 'add a description of u as dog here')
            desc.pack()
        if result == 'blue heron':
            urllib.request.urlretrieve('https://www.wm.edu/as/biology/planttour/_photosets/crimdell/heron.jpg', 'heron.jpeg')
            heron_pic = Image.open('heron.jpeg')
            heron = ImageTk.PhotoImage(heron_pic)
            label = Label(image = heron)
            label.image = heron
            label.pack()
            desc = Label(text = 'add a description of u as heron here')
            desc.pack()

    def next_question(self):
        for i in self.frame.winfo_children():
            i.destroy()
        q = self.counter
        if self.counter < len(questions):
            self.counter += 1
            self.question(questions[q][0], questions[q][1], questions[q][2], questions[q][3], questions[q][4])
        else:
            print('ending')
            self.end()

    

#https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python

#https://stackoverflow.com/questions/44634947/how-to-set-a-turtle-to-a-turtle-screen/44639041#44639041

#root.mainloop()
window = Tk()
window.title('Quiz')
window.geometry('600x400')
quiz = Quiz(window)
#quiz.option1('this is a button!')
window.mainloop()
#print(quiz)

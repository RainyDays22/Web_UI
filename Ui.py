from tkinter import *
import sys
import urllib.request
from PIL import ImageTk, Image
import os


questions = {0:['1 of 10: What’s your favorite snack?', 'Almonds', 'Gummy worms', 'Cookies', 'Goldfish', 'Exit quiz'],
            1:['2 of 10: What’s your favorite season?', 'Fall', '​​Summer', 'Spring', 'Winter', 'Exit quiz'],
            2:['3 of 10: What’s your ideal day?', 'Going shopping', 'Chilling with your friends at the beach', 'Visiting someplace you haven’t been before and meeting new people', 'Solo relaxation day', 'Exit quiz'],
            3:['4 of 10: What’s the square root of 1.2 million?', 'I don’t have the time for your little games', 'Animals don’t do math', '1,095.45', 'The square root of 1.2 million', 'Exit quiz'], 
            4:['5 of 10: What’s your favorite subject in school?', 'Geography', 'Gym', 'Humanities', 'Computer science ;)', 'Exit quiz'], 
            5:['6 of 10: How many hours a night do you sleep?', 'What’s sleep?', 'Zero, I sleep during the day', '8 hours, just what the doctor ordered', 'As much as I need', 'Exit quiz'], 
            6:['7 of 10: What’s your favorite biome?', 'Temperate woodland', 'Tropical rainforest', 'Grassland', 'Freshwater', 'Exit quiz'], 
            7:['8 of 10: What’s your favorite movie genre?', 'Action', 'Mystery', 'Comedy', 'Drama', 'Exit quiz'], 
            8:['9 of 10: Choose a fun emoticon.', '( ͡° ͜ʖ ͡°)', '¯\_(ツ)_/¯', '​​ᕕ( ᐛ )ᕗ', '(◡‿◡✿)', 'Exit quiz'], 
            9:['10 of 10: What’s your favorite place on campus?', 'Sadler', 'Crim Dell', 'Swem', 'ISC', 'Exit quiz']}


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
        exit_btn = Button(self.frame, text="Exit quiz", command=self.exit, fg = 'blue')
        exit_btn = exit_btn.pack(side=TOP)
        
    def exit(self):
        sys.exit()

    def restart(self):
        os.execl(sys.executable, sys.executable, *sys.argv)

    def add_A(self):
        self.answers.append('A')

    def add_B(self):
        self.answers.append('B')

    def add_C(self):
        self.answers.append('C')

    def add_D(self):
        self.answers.append('D')
    
    def question(self, title, option1, option2, option3, option4, option5):
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
        option5 = Button(self.frame, text = option5, command=self.exit, fg = 'blue')
        option5.pack(side=TOP)

    def next_question(self):
        for i in self.frame.winfo_children():
            i.destroy()
        q = self.counter
        if self.counter < len(questions):
            self.counter += 1
            self.question(questions[q][0], questions[q][1], questions[q][2], questions[q][3], questions[q][4], questions[q][5])
        else:
            self.end()

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
        if A_counter > B_counter and A_counter > C_counter and A_counter > D_counter:
            return 'squirrel'
        elif B_counter > A_counter and B_counter > C_counter and B_counter > D_counter:
            return 'frog'
        elif C_counter > A_counter and C_counter > B_counter and C_counter > D_counter:
            return 'Swem therapy dog'
        elif D_counter > A_counter and D_counter > B_counter and D_counter > C_counter:
            return 'blue heron'
        else:
            return 'Griffin'

    def end(self):
        result = self.evaluate()
        title = Label(text = 'You are a ' + str(result) + '!', fg = 'purple')
        title.pack()
        restart_btn = Button(self.frame, text="Take quiz again!", command=self.restart, fg = 'green')
        restart_btn = restart_btn.pack(side=TOP)
        exit_btn = Button(self.frame, text="Exit quiz", command=self.exit, fg = 'blue')
        exit_btn = exit_btn.pack(side=TOP)
        if result == 'squirrel':
            urllib.request.urlretrieve('https://i.imgur.com/PEIFopL.jpg', 'squirrel.jpeg')
            squirrel_pic = Image.open('squirrel.jpeg')
            squirrel_pic.thumbnail((300,300))
            squirrel = ImageTk.PhotoImage(squirrel_pic)
            label = Label(image = squirrel)
            label.image = squirrel
            label.pack()
            desc = Label(text = 'You live life in the fast lane. You’re the type to walk into traffic and somehow emerge totally fine.')
            desc.pack()
            desc2 = Label(text = 'Your hyperactive nature sometimes gets the better of you and you tend to get anxious.')
            desc2.pack()
            desc3 = Label(text = 'You accept that, though, and these traits serve you well when hard times come around.')
            desc3.pack()
        if result == 'frog':
            urllib.request.urlretrieve('https://i.imgur.com/McbobUQ.jpeg', 'frog.jpeg')
            frog_pic = Image.open('frog.jpeg')
            frog_pic.thumbnail((300,300))
            frog = ImageTk.PhotoImage(frog_pic)
            label = Label(image = frog)
            label.image = frog
            label.pack()
            desc = Label(text = 'You know your worth and take up the space you need with no fear.')
            desc.pack()
            desc2 = Label(text = 'Even if you have to battle other frogs or yourself, you’re not one to give up your lily pad.')
            desc2.pack()
            desc3 = Label(text = 'You’re somewhat of a night owl (frog?) and love to just chill and chat.')
            desc3.pack()
            desc4 = Label(text = 'Also you can collect moisture on your skin and drink it, which is definitely super cool and not weird at all.')
            desc4.pack()
        if result == 'Swem therapy dog':
            urllib.request.urlretrieve('https://events.wm.edu/images/event_uploads/sjgilliam_2018_10_04_14_43_59.jpg', 'dog.jpeg')
            dog_pic = Image.open('dog.jpeg')
            dog_pic.thumbnail((300,300))
            dog = ImageTk.PhotoImage(dog_pic)
            label = Label(image = dog)
            label.image = dog
            label.pack()
            desc = Label(text = 'You’re the life of the party. You lift up others around you and brighten a room as soon as you prance in.')
            desc.pack()
            desc2 = Label(text = 'You would do anything to help out a friend in need, even if it means sacrificing some of yourself.')
            desc2.pack()
            desc3 = Label(text = 'You can somehow manage like a hundred different responsibilities at once and still have energy for more.')
            desc3.pack()
        if result == 'blue heron':
            urllib.request.urlretrieve('https://www.wm.edu/as/biology/planttour/_photosets/crimdell/heron.jpg', 'heron.jpeg')
            heron_pic = Image.open('heron.jpeg')
            heron_pic.thumbnail((300,300))
            heron = ImageTk.PhotoImage(heron_pic)
            label = Label(image = heron)
            label.image = heron
            label.pack()
            desc = Label(text = 'You fly solo. Others admire you from afar, which is right where you want them.')
            desc.pack()
            desc2 = Label(text = 'Whether or not it’s true, you appear regal, mysterious, and confident.')
            desc2.pack()
            desc3 = Label(text = 'Although it may get lonely sometimes, you enjoy your own company over anyone else’s.')
            desc3.pack()
            desc4 = Label(text = 'You’re efficient, and can find it frustrating when others can’t keep up with you.')
            desc4.pack()
        if result == 'Griffin':
            urllib.request.urlretrieve('https://www.wm.edu/about/mascot/images/griffin_primary.jpg', 'griffin.jpeg')
            griffin_pic = Image.open('griffin.jpeg')
            griffin_pic.thumbnail((300,300))
            griffin = ImageTk.PhotoImage(griffin_pic)
            label = Label(image = griffin)
            label.image = griffin
            label.pack()
            desc = Label(text = 'You’re so cool and unique that you don’t fit into any category!')
            desc.pack()
            desc2 = Label(text = 'You’re all the best parts of William & Mary rolled into one:')
            desc2.pack()
            desc3 = Label(text = 'independent, clever, confident, and caring.')
            desc3.pack()

if __name__ == '__main__':
    window = Tk()
    window.title('Quiz')
    window.geometry('650x500')
    Quiz(window)
    window.mainloop()
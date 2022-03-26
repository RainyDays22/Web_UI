from turtle import *
import tkinter as tk
screen=Screen()
# add widgets here

class Question:

    class Button:
        def __init__(self):
            self.text = None
            self.image = None
            self.bg = 'blue'
            self.fg = 'purple'
            self.command = None

    def __init__(self):
        self.window = tk.Window()
        self.button = tk.Button(self.window, )

    def title(self, title_text):
        lbl = Label(self.window, text = str(title_text)) #add fg, font
        #lbl.place(x= , y=)
        return lbl

    def option1(self, image, text):
        pass

    def option2(self, image, text):
        pass

    def option3(self, image, text):
        pass

    def option4(self, image, text):
        pass

    

window.title('Hello Python')
window.geometry("300x200+10+20")
window.mainloop()
#https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python

#https://stackoverflow.com/questions/44634947/how-to-set-a-turtle-to-a-turtle-screen/44639041#44639041

import turtle
import tkinter as tk
# add widgets here
root = tk.Tk()
canvas = tk.Canvas(root)
canvas.config(width=600, height=200)
canvas.pack(side=tk.LEFT)
screen = turtle.TurtleScreen(canvas)
screen.bgcolor("cyan")

class Question:

    class Button:
        def __init__(self, image, text):
            self.text = text
            self.image = image
            self.bg = 'blue'
            self.fg = 'purple'
            self.command = None
            return self

    def __init__(self):
        
        #self.button = tk.Button(self.window, )
        #return(self)
        pass
    
    def window(self):
        root = tk.Tk()
        canvas = tk.Canvas(root)
        canvas.config(width=600, height=200)
        canvas.pack(side=tk.LEFT)
        screen = turtle.TurtleScreen(canvas)
        screen.bgcolor("cyan")
    
        return(self)

    def title(self, title_text):
        #lbl = Label(self.window, text = str(title_text)) #add fg, font
        #lbl.place(x= , y=)
        #return lbl
        pass

    def option1(self):
        new_button = self.Button(None, 'Press me')
        button = tk.Button(new_button)
        button.pack()
        return self

    def option2(self, image, text):
        pass

    def option3(self, image, text):
        pass

    def option4(self, image, text):
        pass

    

#https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python

#https://stackoverflow.com/questions/44634947/how-to-set-a-turtle-to-a-turtle-screen/44639041#44639041

root.mainloop()
quiz = Question()
print(quiz.option1())
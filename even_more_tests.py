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
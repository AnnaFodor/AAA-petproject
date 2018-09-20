from tkinter import *
from tkinter import ttk, Canvas, PhotoImage
from PIL import *
from tkinter import filedialog
from os import PathLike
import time
from random import randrange

class Ball:
    def __init__(self, master):
        self.master = master
        color = 'maroon'
        self.shape = master.create_oval(0, 0, 50, 50, fill=color)
        self.speedx = 9
        self.speedy = 9
        self.active = True
        if self.active:
            self.move_active()

    def mouse_and_ball(self, *args):
        if self.active:
            self.speedx *= -1
            self.speedy *= -1

    def ball_update(self):
        self.master.move(self.shape, self.speedx, self.speedy)
        pos = self.master.coords(self.shape)
        if pos[2] >= 1200 or pos[0] <= 0:
            self.speedx *= -1
        if pos[3] >= 600 or pos[1] <= 0:
            self.speedy *= -1

    def move_active(self, event="<Motion>"):
        self.ball_update()
        self.master.after(40, self.move_active)

class Ball2:
    def __init__(self, master):
        self.master = master
        color = 'spring green'
        self.shape = master.create_oval(20, 20, 100, 100, fill=color)
        self.speedx = 15
        self.speedy = 15
        self.active = True
        if self.active:
            self.move_active()

    def mouse_and_ball(self, *args):
        if self.active:
            self.speedx *= -1
            self.speedy *= -1

    def ball_update(self):
        self.master.move(self.shape, self.speedx, self.speedy)
        pos = self.master.coords(self.shape)
        if pos[2] >= 1200 or pos[0] <= 0:
            self.speedx *= -1
        if pos[3] >= 600 or pos[1] <= 0:
            self.speedy *= -1

    def move_active(self, event="<Motion>"):
        self.ball_update()
        self.master.after(40, self.move_active)

def mainBall(*args):
    root = Tk()
    root.title("Ball")
    root.geometry("1200x600")
    root.resizable(0, 0)
    canvas = Canvas(root, width=1200, height=600, bg="khaki")
    canvas.pack()
    exitButton = Button(root, text="Exit")
    ball = Ball(canvas)
    ball2 = Ball2(canvas)
    # exitButton.bind("<Button->", quit)
    # exitButton.pack()
    root.bind("<Button-1>", ball.mouse_and_ball)
    root.bind("<Button-3>", ball2.mouse_and_ball)
    root.mainloop()

class Fish:
    def __init__(self, master):
        self.master = master
        self.create_fish_shape("fish0", randrange(10, 1200), randrange(10, 300), 2, 'SkyBlue1')
        # self.create_fish_shape("fish1", randrange(10, 1200), randrange(10, 450), 1.5, 'gold')
        # self.create_fish_shape("fish2", randrange(10, 1200), randrange(10, 600), 1, 'blue4')
        self.speedx = 15
        self.speedy = 0
        self.active = True
        if self.active:
            self.move_active()

    def create_fish_shape(self, fish_name, fish_x, fish_y, scale, color, *args):
        self.body = self.master.create_oval(fish_x, fish_y, fish_x + 120, fish_y + 70, outline=color, fill=color)
        self.tail = self.master.create_polygon(fish_x + 120, fish_y + 35, fish_x + 140, fish_y + 60, fish_x + 140, fish_y + 10, outline=color, fill=color)
        self.eye = self.master.create_oval(fish_x + 20, fish_y + 20, fish_x + 30, fish_y + 30, outline="black", fill="black")
        self.master.addtag_withtag(fish_name, self.body)
        self.master.addtag_withtag(fish_name, self.tail)
        self.master.addtag_withtag(fish_name, self.eye)
        self.master.scale(fish_name, scale, scale, scale, scale)

    def fishMove(self, *args):
        self.master.move(self.body, self.speedx, self.speedy)
        self.master.move(self.tail, self.speedx, self.speedy)
        self.master.move(self.eye, self.speedx, self.speedy)
        pos = self.master.coords(self.body)
        if pos[2] >= 1200 or pos[0] <= 0:
            self.speedx *= -1
        # self.master.move("fish0", -3, 0)
        # self.master.move("fish1", self.speedx, self.speedy)
        # self.master.move("fish2", self.speedx, self.speedy)
        # root.update()
        # time.sleep(0.010)

    def move_active(self, event="<Motion>"):
        self.fishMove()
        self.master.after(40, self.move_active)

    # def fishAndWall(*args):
    #     if something:
    #         for fish_num in range(3):
    #             (fish_x, fish_y, fish_x2, fish_y2) = c.coords("fish" + str(fish_num))
    #             if fish_x2 < 0:
    #                 if fish_y < 400:
    #                     c.move("fish" + str(fish_num), 1800, randrange(10, 300))
    #                 else:
    #                     c.move("fish" + str(fish_num), 1800, -300)

class Fish2:
    def __init__(self, master):
        self.master = master
        # self.create_fish_shape("fish0", randrange(10, 1200), randrange(10, 300), 2, 'SkyBlue1')
        self.create_fish_shape("fish1", randrange(10, 1200), randrange(10, 450), 1.5, 'gold')
        # self.create_fish_shape("fish2", randrange(10, 1200), randrange(10, 600), 1, 'blue4')
        self.speedx = 20
        self.speedy = 0
        self.active = True
        if self.active:
            self.move_active()

    def create_fish_shape(self, fish_name, fish_x, fish_y, scale, color, *args):
        self.body = self.master.create_oval(fish_x, fish_y, fish_x + 120, fish_y + 70, outline=color, fill=color)
        self.tail = self.master.create_polygon(fish_x + 120, fish_y + 35, fish_x + 140, fish_y + 60, fish_x + 140, fish_y + 10, outline=color, fill=color)
        self.eye = self.master.create_oval(fish_x + 20, fish_y + 20, fish_x + 30, fish_y + 30, outline="black", fill="black")
        self.master.addtag_withtag(fish_name, self.body)
        self.master.addtag_withtag(fish_name, self.tail)
        self.master.addtag_withtag(fish_name, self.eye)
        self.master.scale(fish_name, scale, scale, scale, scale)

    def fishMove(self, *args):
        self.master.move(self.body, self.speedx, self.speedy)
        self.master.move(self.tail, self.speedx, self.speedy)
        self.master.move(self.eye, self.speedx, self.speedy)
        pos = self.master.coords(self.body)
        if pos[2] >= 1200 or pos[0] <= 0:
            self.speedx *= -1
        # self.master.move("fish0", -3, 0)
        # self.master.move("fish1", self.speedx, self.speedy)
        # self.master.move("fish2", self.speedx, self.speedy)
        # root.update()
        # time.sleep(0.010)

    def move_active(self, event="<Motion>"):
        self.fishMove()
        self.master.after(40, self.move_active)

def mainFish(*args):
    root = Tk()
    root.title('Aquarium')
    root.geometry("1200x600")
    root.resizable(0, 0)
    canvas = Canvas(root, width=1200, height=600, bg='DeepSkyBlue2')
    canvas.pack()
    fish1 = Fish(canvas)
    fish2 = Fish2(canvas)
    #bubble = create_bubble()
    root.mainloop()

def todo(*args):
    root = Tk()
    root.title("To Do")
    root.geometry("1200x600")
    canvas = Canvas(root, width=1200, height=600, bg='DeepSkyBlue2')
    # root.configure(background="gold2")
    root.resizable(0, 0)

    top_label = Label(root, text="To Do", bg="white")
    top_label.pack()
    label_space = Label(root, text="", bg="white")
    label_space.pack()
    txt_input = Entry(root, width=15)
    txt_input.pack()

    txt_input_button = Button(root, text="Save", fg="blue", bg="white", command=add_task)
    txt_input_button.pack()
    txt_delete_button = Button(root, text="Delete", fg="blue", bg="white", command=delete_button)
    txt_delete_button.pack()
    exit_button = Button(root, text="Save", fg="blue", bg="white", command=quit)
    exit_button.pack()
    task_lists = Listbox(root)
    task_lists.pack()
    root.mainloop()    

def main():
    root = Tk()

    root.title("Our last week project in ProgBasics")
    root.configure(background="RoyalBlue2")
    root.geometry("1200x600")
    root.resizable(0, 0)

    canvas = Canvas(root, width=550, height=250, bg="RoyalBlue2", highlightthickness=0)
    canvas.pack()

    # logo = PhotoImage(file="aaa-logo-500x.png")
    # canvas.create_image(0, 0, anchor=NW, image=logo)

    var_1 = StringVar()
    label = ttk.Label(relief="solid", font='Times 22 bold', textvariable=var_1)
    label.pack()
    var_1.set("Select button to waste your time")

    top_frame = Frame(root)
    top_frame.pack(side=LEFT)

    button_frame = Frame(root)
    button_frame.pack(side=RIGHT)

    buttom_top_quic = Frame(root)
    buttom_top_quic.pack(anchor=S)


    button_game_1 = Button(top_frame, text="Ball", fg="red", bg="cyan3", highlightthickness=0)
    button_game_1.bind('<Button-1>', mainBall)
    button_game_1.pack()

    button_game_2 = Button(button_frame, text="Aquarium", fg="red", bg="cyan3", highlightthickness=0)
    button_game_2.bind("<Button-1>", mainFish)
    button_game_2.pack()

    button_game_3 = Button(text="Annamari", fg="red", bg="cyan3", highlightthickness=0)
    button_game_3.bind("<Button-1>", todo)
    button_game_3.pack()

    main_menu = Menu(root)

    root.configure(menu=main_menu)

    sub_manu = Menu(main_menu)

    main_menu.add_cascade(label="File", menu=sub_manu)

    sub_manu.add_cascade(label="Annamari's game")

    sub_manu.add_cascade(label="Alina's game")

    sub_manu.add_cascade(label="Anna's game")

    close = Button(buttom_top_quic, text='Quit', bg='SeaGreen2', fg='black', highlightthickness=0, command=lambda: quit()).pack()

    root.mainloop()


if __name__ == '__main__':
    main()
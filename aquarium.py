from tkinter import *
import time
from random import randrange


def create_fish_shape(fish_name, fish_x, fish_y, scale, color):
    body = c.create_oval(fish_x, fish_y, fish_x + 120, fish_y + 70, outline=color, fill=color)
    tail = c.create_polygon(fish_x + 120, fish_y + 35, fish_x + 140, fish_y + 60, fish_x + 140, fish_y + 10, outline=color, fill=color)
    eye = c.create_oval(fish_x + 20, fish_y + 20, fish_x + 30, fish_y + 30, outline="black", fill="black")
    c.addtag_withtag(fish_name, body)
    c.addtag_withtag(fish_name, tail)
    c.addtag_withtag(fish_name, eye)
    c.scale(fish_name, scale, scale, scale, scale)

    
'''
def create_bubble():
    bubble = c.create_oval(400, 350, 410, 340, outline='SkyBlue1')
    return bubble
'''

root = Tk()
root.title('Aquarium')
c = Canvas(root, width=1400, height=800, background='DeepSkyBlue2')
create_fish_shape("fish0", randrange(10, 1200), randrange(10, 300), 2, 'SkyBlue1')
create_fish_shape("fish1", randrange(10, 1200), randrange(10, 450), 1.5, 'gold')
create_fish_shape("fish2", randrange(10, 1200), randrange(10, 600), 1, 'blue4')
#bubble = create_bubble()


c.pack()


while True:
    c.move("fish0", -3, 0)
    c.move("fish1", -2, 0)
    c.move("fish2", -1, 0)
    root.update()
    time.sleep(0.010)

    for fish_num in range(3):
        (fish_x, fish_y, fish_x2, fish_y2) = c.coords("fish" + str(fish_num))
        if fish_x2 < 0:
            if fish_y < 400:
                c.move("fish" + str(fish_num), 1800, randrange(10, 300))
            else:
                c.move("fish" + str(fish_num), 1800, -300)
        

root.mainloop()

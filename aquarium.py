from tkinter import *

root = Tk()
root.title('Anna')
c = Canvas(root, width=900, height=600, background='DeepSkyBlue2')

c.body_color = 'SkyBlue1'
body = c.create_oval(400, 350, 520, 420, outline=c.body_color, fill=c.body_color)
tail = c.create_polygon(500, 385, 540, 410, 540, 360, outline=c.body_color, fill=c.body_color)
eye = c.create_oval(420, 370, 430, 380, outline= "black", fill= "black")

c.pack()

root.mainloop()

from tkinter import *
window=Tk()
c=Canvas(window,width=300,height=300)
c.pack()
c.create_line(0,0,300,300,fill="red")
c.create_line(300,0,0,300,fill="red")
c.create_rectangle(0,0,100,100 ,fill="red")
c.create_oval(10,10,100,100,fill="red")
window.mainloop()

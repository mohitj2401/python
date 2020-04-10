from tkinter import *
window=Tk()
def PrintValue():
    print(uservar.get())
# uservar=StringVar()
# uservar.trace("w",lambda name,index,mode:PrintValue()
labelUser=Label(window,text="Username : ")
labelPass=Label(window,text="Password : ")
labelUser.grid(row=0,sticky=W)
labelPass.grid(row=2,sticky=W)
eUser= Entry(window)
eUser.grid(row=0,column=1)

ePass=Entry(window)
ePass.grid(row=2,column=1)
window.mainloop()


from tkinter import *

class Root(Tk):
    def __init__(self):

        super().__init__()
        self.title("your app in desktop")
        self.minsize(640,320)
        self.configure(background="#3d3d3d")
        self.init_uni()
    def init_uni(self):
        label1 = Label(self,bg="#101010",fg="#5d5d5d",text="hi im use tk in windows (haha)")
        label1.grid(column=0,row=0)
       

window = Root()
window.mainloop()


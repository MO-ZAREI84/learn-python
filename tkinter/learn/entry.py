from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("Your App in Desktop")
        self.minsize(640, 320)
        self.configure(background="#3d3d3d")
        self.count = 0  # شمارنده دکمه
        self.init_ui()

    def init_ui(self):
        pass

window = Root()
window.mainloop()

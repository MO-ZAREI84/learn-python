from tkinter import *

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        self.minsize(640, 320)
        self.init_ui()

    def init_ui(self):
        self.username = StringVar()

        self.label = Label(self, text="Please enter username: ")
        self.label.grid(column=0, row=0)

        entry = Entry(self, textvariable=self.username)
        entry.grid(column=1, row=0)

        submit_btn = Button(self, text="SUBMIT", command=self.submit_username)
        submit_btn.grid(column=2, row=0)

    def submit_username(self):
        self.label.config(text=f"your username is: {self.username.get()}")

window = Root()
window.mainloop()
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
        # دکمه‌ای که به `button_click` متصل شده
        bt1 = ttk.Button(self, text="Submit", command=self.button_click)
        bt1.grid(column=1, row=0, padx=10, pady=10)

        # لیبلی که متنش تغییر می‌کنه
        self.label1 = ttk.Label(self, text="OK start; let's gooooo")
        self.label1.grid(column=0, row=0, padx=10, pady=10)

    def button_click(self):
        self.count += 1
        self.label1.configure(text=f"Count: {self.count}")

window = Root()
window.mainloop()

import tkinter as tk

# تابع برای انجام عملیات ریاضی
def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)  # پاک کردن ورودی
    entry.insert(tk.END, current + value)  # اضافه کردن مقدار جدید به ورودی

# تابع برای محاسبه نتیجه
def calculate():
    try:
        result = eval(entry.get())  # محاسبه مقدار ورودی
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "خطا!")

# تابع برای پاک کردن ورودی
def clear():
    entry.delete(0, tk.END)

# ساخت پنجره اصلی
root = tk.Tk()
root.title("ماشین حساب")
root.geometry("400x500")
root.configure(bg="#F4F4F4")

# ورودی نمایش اعداد و عملگرها
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# دکمه‌ها
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# اضافه کردن دکمه‌ها به پنجره
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda value=text: click_button(value) if value != "=" else calculate())
    button.grid(row=row, column=col, padx=5, pady=5)

# دکمه حذف
clear_button = tk.Button(root, text="C", width=5, height=2, font=("Arial", 18), command=clear)
clear_button.grid(row=5, column=0, padx=5, pady=5)

# اجرای برنامه
root.mainloop()

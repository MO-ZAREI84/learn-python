import tkinter as tk

# تابع برای انجام عملیات ریاضی
def calculate():
    try:
        result = eval(entry.get())  # محاسبه مقدار ورودی
        label_result.config(text=f"نتیجه: {result}")
    except Exception as e:
        label_result.config(text="خطا!")

# ساخت پنجره اصلی
root = tk.Tk()
root.title("ماشین حساب")
root.geometry("300x200")

# ورودی اعداد و عملگرها
entry = tk.Entry(root, width=20, font=("Arial", 14))
entry.pack(pady=10)

# دکمه محاسبه
btn = tk.Button(root, text="محاسبه", command=calculate, font=("Arial", 12))
btn.pack(pady=5)

# لیبل نمایش نتیجه
label_result = tk.Label(root, text="نتیجه: ", font=("Arial", 14))
label_result.pack(pady=10)

# اجرای برنامه
root.mainloop()

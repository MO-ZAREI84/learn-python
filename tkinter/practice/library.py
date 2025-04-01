import sqlite3
import tkinter as tk
from tkinter import messagebox

# ایجاد پایگاه داده
conn = sqlite3.connect("library.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL)''')
conn.commit()

# تابع برای اضافه کردن کتاب
def add_book():
    title = title_entry.get()
    author = author_entry.get()

    if title and author:
        cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        conn.commit()
        title_entry.delete(0, tk.END)
        author_entry.delete(0, tk.END)
        show_books()
    else:
        messagebox.showwarning("خطا", "لطفاً نام کتاب و نویسنده را وارد کنید.")

# نمایش لیست کتاب‌ها
def show_books():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT id, title, author FROM books")
    for book in cursor.fetchall():
        listbox.insert(tk.END, f"{book[0]}. {book[1]} - {book[2]}")

# حذف کتاب
def delete_book():
    selected = listbox.curselection()
    if selected:
        book_id = listbox.get(selected[0]).split('.')[0]  # استخراج id
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        show_books()
    else:
        messagebox.showwarning("خطا", "لطفاً یک کتاب را انتخاب کنید.")

# ایجاد پنجره
root = tk.Tk()
root.title("کتابخانه شخصی")

# ورودی‌ها
tk.Label(root, text="نام کتاب:").grid(row=0, column=0)
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1)

tk.Label(root, text="نویسنده:").grid(row=1, column=0)
author_entry = tk.Entry(root)
author_entry.grid(row=1, column=1)

# دکمه‌ها
tk.Button(root, text="افزودن کتاب", command=add_book).grid(row=2, column=0, columnspan=2)
tk.Button(root, text="حذف کتاب", command=delete_book).grid(row=3, column=0, columnspan=2)

# لیست نمایش کتاب‌ها
listbox = tk.Listbox(root, width=50)
listbox.grid(row=4, column=0, columnspan=2)
show_books()

root.mainloop()

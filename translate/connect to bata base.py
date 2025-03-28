from pathlib import Path
import json
import sqlite3

# خواندن محتوای فایل JSON
data = Path("data.json").read_text()
word_list = json.loads(data)  # تبدیل JSON به دیکشنری

# اتصال به دیتابیس
with sqlite3.connect("my_app.db") as conn:
    cursor = conn.cursor()

    # ایجاد جدول اگر وجود ندارد
    command_table = '''
    CREATE TABLE IF NOT EXISTS translate (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT,
        meaning TEXT
    );
    '''
    cursor.execute(command_table)

    # دستور INSERT برای اضافه کردن داده‌ها
    command = "INSERT INTO translate (word, meaning) VALUES (?, ?)"

    for word, meanings in word_list.items():
        for meaning in meanings:
            cursor.execute(command, (word, meaning))  # ذخیره هر معنی به‌صورت جداگانه

    conn.commit()  # ذخیره تغییرات

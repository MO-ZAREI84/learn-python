from pathlib import Path

import sqlite3

data = Path("data.json").read_text()


def get_user_input():
    word = input("please enter a word: ")
    return word

def search_in_dictionary(w):
    with sqlite3.connect("my_app.db") as conn:
        cursor = conn.cursor()
        command = " SELECT * FROM translate WHERE word=? "
        cursor.execute(command, (w,) )
        rows = cursor.fetchall()
        for row in rows:
            print(row[2])

word = get_user_input()
search_in_dictionary(word)
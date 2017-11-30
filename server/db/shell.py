"""A minimal SQLite shell for experiments
"""
import sqlite3

con = sqlite3.connect("map.db")
con.isolation_level = None
cur = con.cursor()

buffer = ""

print("Enter your SQL commands to execute in sqlite3.\n"
      "Enter a blank line to exit.")

while True:
    line = input()
    if line == "":
        break
    buffer += line
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            cur.execute(buffer)

            if buffer.lstrip().upper().startswith("SELECT"):
                for line in cur.fetchall():
                    print(line)
        except sqlite3.Error as e:
            print("An error occurred: {}".format(e.args[0]))
        buffer = ""

con.close()

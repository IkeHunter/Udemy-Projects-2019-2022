import sqlite3

conn = sqlite3.connect("contacts.sqlite")

query_name = input("Please enter the name: ")

# conn.execute("SELECT * FROM sqlite_master")

# for row in conn.execute("SELECT * FROM contacts WHERE name = ?", (query_name,)):
for row in conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (query_name,)):
    print(row)

conn.close()

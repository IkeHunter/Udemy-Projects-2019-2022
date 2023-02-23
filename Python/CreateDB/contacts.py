import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('ike', 6545678, 'ike@mail.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@mail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
# for row in cursor:
#     print(row)

# print(cursor.fetchall())  # creates a list of tuples of the data

print(cursor.fetchone())  # returns single row in a tuple

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

cursor.close()
db.commit()
db.close()

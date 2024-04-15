import csv
import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT
                )''')

csv_file = 'users.csv'
with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        name = row.get('name')
        email = row.get('email')
        if name and email:
            cursor.execute('''INSERT INTO users (name, email) VALUES (?, ?)''', (name, email))

conn.commit()
conn.close()

print("Data from CSV file inserted into DB successfully.")

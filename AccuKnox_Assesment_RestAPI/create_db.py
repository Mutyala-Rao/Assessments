import sqlite3


# Function to create a SQLite database and insert sample data
def create_sample_database():
    try:
        conn = sqlite3.connect("books.db")
        c = conn.cursor()
        # Create a table named 'books' if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS books
                     (id INTEGER PRIMARY KEY, title TEXT, author TEXT, publication_year INTEGER)''')

        # Sample data to insert into the 'books' table
        sample_books = [
            ("To Kill a Mockingbird", "Harper Lee", 1960),
            ("1984", "George Orwell", 1949),
            ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
            ("Pride and Prejudice", "Jane Austen", 1813),
            ("The Catcher in the Rye", "J.D. Salinger", 1951)
        ]

        # Insert the sample data into the 'books' table
        c.executemany('''INSERT INTO books (title, author, publication_year)
                         VALUES (?, ?, ?)''', sample_books)

        conn.commit()
        print("Sample database created successfully.")
    except sqlite3.Error as e:
        print("Error creating sample database:", e)
    finally:
        conn.close()


# Call the function to create the sample database
create_sample_database()

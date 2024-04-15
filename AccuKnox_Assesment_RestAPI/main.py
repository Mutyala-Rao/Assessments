import sqlite3
import os.path
import requests

# Function to check if the database exists
def database_exists():
    return os.path.exists("books.db")

# Function to create a SQLite database and table
def create_database():
    try:
        conn = sqlite3.connect("books.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS books
                     (id INTEGER PRIMARY KEY, title TEXT, author TEXT, publication_year INTEGER)''')
        conn.commit()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating database:", e)

# Function to fetch data from an external API
def fetch_books_from_api(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.RequestException as e:
        print("Error fetching data from the API:", e)
        return None

# Function to display the retrieved data
def display_books(books):
    if books:
        print("Retrieved books from the API:")
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}, Publication Year: {book['publication_year']}")
    else:
        print("No books retrieved from the API.")

# Function to insert data into the SQLite database
def insert_books_into_db(books):
    try:
        conn = sqlite3.connect("books.db")
        c = conn.cursor()
        for book in books:
            c.execute('''INSERT INTO books (title, author, publication_year)
                         VALUES (?, ?, ?)''', (book['title'], book['author'], book['publication_year']))
        conn.commit()
        print("Data inserted into the database successfully.")
    except sqlite3.Error as e:
        print("Error inserting data into the database:", e)
    finally:
        conn.close()

# Main function
def main():
    # Example API URL
    api_url = "http://127.0.0.1:5000/books"

    # Check if the database exists
    if not database_exists():
        # Create the database and table if they don't exist
        create_database()

    # Fetch books from the API
    books_data = fetch_books_from_api(api_url)

    # Display retrieved data from the API
    display_books(books_data)

    if books_data:
        # Insert fetched books into the database
        insert_books_into_db(books_data)
    else:
        print("Failed to fetch books from the API.")

if __name__ == "__main__":
    main()

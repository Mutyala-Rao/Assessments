from flask import Flask, jsonify

app = Flask(__name__)

# Sample list of books
books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "publication_year": 1960},
    {"title": "1984", "author": "George Orwell", "publication_year": 1949},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "publication_year": 1925},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "publication_year": 1813},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "publication_year": 1951}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)

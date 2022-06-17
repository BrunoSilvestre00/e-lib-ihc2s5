from flask import Flask, render_template, request
import json
import webbrowser

app = Flask(__name__)
BOOKS = None

@app.route('/book-detail/<book_id>')
def book_detail(book_id):
    book = BOOKS[f'book_{book_id}']
    return render_template('book_detail.html', book=book)

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    # webbrowser.open('http://127.0.0.1:5000/book-detail/1')
    webbrowser.open('http://127.0.0.1:5000/home')
    with open('resources-data.json', 'r', encoding='utf-8') as f:
        BOOKS = json.load(f)
    app.run()
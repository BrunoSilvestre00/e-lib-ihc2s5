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
    CAROUSEL_LIST = ['img_ex1.jpg', 'img_ex2.jpg', 'img_ex3.jpg']
    BOOKS_FOR_YOU = [BOOKS[f'book_{i}'] for i in [7, 11, 13, 14, 18, 9, 2]]
    BOOKS_HORROR = [BOOKS[f'book_{i}'] for i in [4, 5, 6, 10, 15, 19]]
    BOOKS_HAPPY = [BOOKS[f'book_{i}'] for i in [1, 3, 8, 12, 16, 17]]
    return render_template('home.html', carousel_list=CAROUSEL_LIST, for_you=BOOKS_FOR_YOU, horror=BOOKS_HORROR, happy=BOOKS_HAPPY)

if __name__ == '__main__':
    # webbrowser.open('http://127.0.0.1:5000/book-detail/1')
    webbrowser.open('http://127.0.0.1:5000/home')
    with open('resources-data.json', 'r', encoding='utf-8') as f:
        BOOKS = json.load(f)
    app.run()
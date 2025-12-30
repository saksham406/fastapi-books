from fastapi import FastAPI

app = FastAPI() # allow to use fastapi pacakges

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books/read_all_books/")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}/") #adding decorator to call this function
async def read_book(book_title: str): # asycn is not needed in fastapi because it will asycn behine scenes
    for book in BOOKS:
        if book['title'].lower() == book_title.lower():
            return book

@app.get("/books/my_books/")
async def get_my_favourite_book():
    return {
        'my books': 'My Favourite Book'
    }
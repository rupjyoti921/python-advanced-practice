from fastapi import FastAPI

app= FastAPI()

BOOKS=[
    {"title":"title_one", "author":"author_one", "category":"Science"}, 
    {"title":"title_two", "author":"author_two", "category":"Biology"},  
    {"title":"title_three", "author":"author_three", "category":"Computer"}  

]

# normal get request for all books
@app.get("/books")
async def all_books():
    return BOOKS

# get request for one book
@app.get("/books/{onebook}")
async def one_book(onebook:str):
    for book in BOOKS:
        if book.get("title").casefold() == onebook.casefold():
            return book

# get request using query
@app.get("/books/")
async def read_book_by_query(category:str):
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            return book
from fastapi import Body,FastAPI

app= FastAPI()

BOOKS=[
    {"title":"title_one", "author":"author_one", "category":"Science"}, 
    {"title":"title_two", "author":"author_two", "category":"Biology"},  
    {"title":"title_three", "author":"author_three", "category":"Computer"},
    {"title":"title_four", "author":"author_four", "category":"Science"},   

]


#------------------------------------------PUT HTTP REQUEST---------------------------------
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold()==updated_book.get("title").casefold():
            BOOKS[i]=updated_book

#------------------------------------------POST HTTP REQUEST---------------------------------
@app.post("/books/create_book")
async def create_new_book(new_book=Body()):
    BOOKS.append(new_book)
    return BOOKS

#-------------------------------------------GET HTTP REQUEST---------------------------------
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
    books_to_return=[]
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return        

# get request using dynamic parameter and query both
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author:str, category: str):
    for book in BOOKS:
        if book.get("author").casefold()==book_author.casefold() and book.get("category").casefold()==category.casefold():
            return book
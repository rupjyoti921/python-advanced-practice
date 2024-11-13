from fastapi import FastAPI

app= FastAPI()

BOOKS=[
    {"title1":"title_one", "author1":"author_one", "category1":"Science"}, 
    {"title2":"title_two", "author2":"author_two", "category2":"Biology"},  
    {"title3":"title_three", "author3":"author_three", "category3":"Computer"}  

]

@app.get("/books")
async def all_books():
    return BOOKS
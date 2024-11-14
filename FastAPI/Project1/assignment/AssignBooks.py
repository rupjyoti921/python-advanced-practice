from fastapi import Body, FastAPI

BOOKS=[
    {"title":"title_one", "author":"author_one", "category":"Science"}, 
    {"title":"title_two", "author":"author_two", "category":"Biology"},  
    {"title":"title_three", "author":"author_three", "category":"Computer"},
    {"title":"title_four", "author":"author_four", "category":"Science"},
    {"title":"title_five", "author":"author_five", "category":"English"}  

]

app=FastAPI()


from fastapi import FastAPI

class Book:
    id:int
    title:str
    author:str
    desc:str
    rating:int

def __init__(self,Id,Title,Author,Desc,Rating):
    self.id=Id
    self.title=Title
    self.author=Author
    self.desc=Desc
    self.rating=Rating
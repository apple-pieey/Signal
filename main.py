from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from oracleDB import OracleDB
from pydantic import BaseModel

class novel(BaseModel):
    novel_no : int
    novel_nm : str
    novel_writer : str
    novel_synopsis : str
    novel_cover : str

db = OracleDB()

app = FastAPI()
templates = Jinja2Templates(directory="RomanPick")
app.mount("/static", StaticFiles(directory="RomanPick/static"), name="static")


@app.get("/")
def read_root(request:Request):
    return templates.TemplateResponse('index.html',{"request" : request})

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

# @app.get("/aa/")
# def aa():
#     return 'aaaaaaaaaaaaaaaaaaaaaaaaaaaa'

# @app.get("/item")
# def insert_item():
#     db.execute_insert(book.dict())
#     print(book)
#     return  {"message": "Book inserted successfully"}

@app.get("/book")
def insert_item(num:int, title:str):
    values = {"num": num, "title": title}
    db.execute_insert1(values)
    return  {"message": "Book inserted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
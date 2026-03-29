from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def greet():
  return {"Message":"Hello from Docker"}

@app.get("/items/{item_id}")
def get_by_id(item_id:int):
  return {"item_id":item_id}



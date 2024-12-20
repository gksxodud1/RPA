from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"늦음" : "운동 혼자가라"}

@app.get("/item")
def read_item(item_id: int, name: str = None, age: int = 0):
    return {"item_id": item_id,"name": name, "age": age}

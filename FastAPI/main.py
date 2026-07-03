from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
      return{"meassage":"hello without vern"}
import sqlite3
from fastapi import FastAPI
app=FastAPI()
connect=sqlite3.connect("test.db",check_same_thread=False)#first parameter will be file name where data stores 
#and second parameter tells check same thread not update same things 
cursor=connect.cursor()#here in sqlite cursor will run the sql query
#now table creation
cursor.execute("""
        create table if not exists todos(
        id INTEGER PRIMARY KEY,
        title TEXT,
        completed TEXT)
        """)
connect.commit()#Here data base updated
@app.get("/")
def home():
    return{
        "message":"SQLite connected fine"
    }
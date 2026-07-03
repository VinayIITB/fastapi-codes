from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
#This is the first class where all the things are present 
class User(BaseModel):
    name:str
    age:int
    password:str
    
#then response model send the data it hide the information that is need 
# to hide from the client
class UserResponse(BaseModel):
    name:str
    age:int
    
@app.get("/user",response_model=UserResponse)

def get_user():
    return{
        "name":"Vinay",
        "age":20,
        "password":"1234"
    }
from fastapi import FastAPI,status,HTTPException
app=FastAPI()

@app.post("/create_user",status_code=status.HTTP_201_CREATED)

def create_user():
    return{
        "message":"user created"
    }
    
@app.get("/user")
def user():
    return{
        "status":"sucess",
        "message":"user fetched",
        "data":{
            "name":"vinay",
            "age":24
        }
    }

# it is for error handling and this get api is for user id
@app.get("/users/{user_id}")
def get_staus(user_id:int):
    if user_id!=1:
        raise HTTPException(
            status_code=404,
            detail="users not found"
        )
    return{
        "id":1,
        "name":"Mohit"
    }
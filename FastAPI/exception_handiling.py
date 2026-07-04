from fastapi import FastAPI,HTTPException,Request

from fastapi.responses import JSONResponse

app=FastAPI()

#exception raising informaton stored here 
class UserNotFoundException(Exception):
    def __init__(self,name:str):
        self.name=name

@app.get("/user/{name}")
def get_user(name:str):
    if name != "mohit":
        raise UserNotFoundException(name)
    return{
        "name":"mohit"
    }
    
#exception handler 
@app.exception_handler(UserNotFoundException)
def User_not_found_handler(request:Request,exec:UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"User {exec.name} not found"
        }
    )
# @app.get("/user/{user_id}")

# def get_user(user_id:int):
#     if user_id != 1:
#         raise HTTPException(
#             status_code=404,
#             detail="user not found"
#         )
#     return{
#         "id":1,
#         "name":"mohit"
#     }
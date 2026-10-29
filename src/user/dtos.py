from pydantic import BaseModel

class userSchema(BaseModel):
    username : str
    name: str
    email: str
    password : str
    

class userResponseSchema(BaseModel):
    username : str
    name: str
    email: str
    id : int
    
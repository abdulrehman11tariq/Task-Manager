from pydantic import BaseModel

class userSchema(BaseModel):
    username : str
    name: str
    email: str
    password : str
    
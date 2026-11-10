from pydantic import BaseModel, Field, EmailStr

class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
from pydantic import BaseModel


class UserBase(BaseModel):
    firstname: str
    lastname: str
    username: str
    email: str
    phone: str


class UserCreate(UserBase):
    notification: int
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class NotificationCreate(BaseModel):
    notification: str


class Notification(NotificationCreate):
    id: int

    class Config:
        orm_mode = True

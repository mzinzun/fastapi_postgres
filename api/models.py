from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    notification = Column(String(150))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(150))
    lastname = Column(String(150))
    username = Column(String(150), unique=True)
    email = Column(String(150), unique=True)
    phone = Column(String(15))
    notification = Column(Integer, ForeignKey("notifications.id"))
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import sessionLocal, engine
import schemas
import queries
import models

router = APIRouter()
models.Base.metadata.create_all(bind=engine)

# for route Dependancy
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = queries.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return queries.create_user(db=db, user=user)


@router.get("/users/", response_model=list[schemas.User])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = queries.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.User)
def show_user(user_id: int, db: Session = Depends(get_db)):
    db_user = queries.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/notifications/", response_model=schemas.Notification)
def create_notification(notification: schemas.NotificationCreate, db: Session = Depends(get_db)):
    return queries.create_notification(db=db, notification=notification)

@router.get("/notifications/", response_model=list[schemas.Notification])
def list_notifications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notifications = queries.get_notifications(db, skip=skip, limit=limit)
    return notifications

from sqlalchemy.orm import Session
import models
import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password+"notreallyhashed"
    db_user = models.User(
        firstname=user.firstname,
        lastname=user.lastname,
        username=user.username,
        email=user.username,
        phone=user.phone,
        hashed_password=fake_hashed_password
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_notification(db: Session, notif_id: int):
    return db.query(models.Notification).filter(models.Notification.id == notif_id).first()


def get_notifications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Notification).offset(skip).limit(limit).all()


def create_notification(db: Session, notification: schemas.NotificationCreate):
    db_notif = models.Notification(
        notification=notification.notification
    )
    db.add(db_notif)
    db.commit()
    db.refresh(db_notif)
    return db_notif

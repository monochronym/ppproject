from sqlalchemy.orm import Session

import db_interraction.models as models
import db_interraction.schemas as schemas
import utils
import uuid


def get_user(db: Session, user_id: uuid.UUID):
    return db.query(models.User).filter(models.User.uuid == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_id(db: Session, id: uuid.UUID):
    return db.query(models.User).filter(models.User.uuid == id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_videos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Video).offset(skip).limit(limit).all()


def get_videos_by_name(db: Session, name: str):
    return db.query(models.Video).filter(models.Video.name.like(f"%{name}%"))

def get_brands(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Brand).offset(skip).limit(limit).all()

def get_goods(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Good).offset(skip).limit(limit).all()

def get_news(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.News).offset(skip).limit(limit).all()



def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    hashed_password, salt = utils.hash_password(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password, salt=salt, uuid=uuid.uuid4(),
                          username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_video(db: Session, video: schemas.Video) -> models.Video:
    db_video = models.Video(id=video.id, image=video.image_path, video=video.video_path, user=video.user,
                            name=video.name)
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video


def create_good(db: Session, good: schemas.Good) -> models.Good:
    db_good = models.Good(goodname=good.goodname, gooduuid=good.gooduuid, branduuid=good.branduuid,
                          description=good.description)
    db.add(db_good)
    db.commit()
    db.refresh(db_good)
    return db_good


def create_brand(db: Session, brand: schemas.Brand) -> models.Brand:
    db_brand = models.Good(goodname=brand.brandname, gooduuid=brand.branduuid, description=brand.description)
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand


def create_news(db: Session, news: schemas.News) -> models.News:
    db_news = models.Good(posteduser=news.posteduser, newsuuid=news.newsuuid, posttext=news.posttext)
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

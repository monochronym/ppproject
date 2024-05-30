from sqlalchemy import Boolean, Column, String, UUID, Integer

from db_interraction.database import Base


class User(Base):
    __tablename__ = "users"

    username = Column(String, unique=True, index=True)
    uuid = Column(UUID, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    salt = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(Integer, default=0)


class Video(Base):
    __tablename__ = "videos"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String)
    image = Column(String, unique=True, index=True)
    video = Column(String, unique=True, index=True)
    user = Column(String, index=True)


class Good(Base):
    __tablename__ = "goods"

    goodname = Column(String)
    gooduuid = Column(UUID, primary_key=True, index=True)
    branduuid = Column(UUID)
    description = Column(String)

class Brand(Base):

    __tablename__ = "brands"

    brandname = Column(String)
    branduuid = Column(UUID, primary_key=True, index=True)
    description = Column(String)

class News(Base):

    __tablename__ = "news"

    posteduser = Column(UUID)
    posttext = Column(String)
    newsuuid = Column(UUID, primary_key=True)



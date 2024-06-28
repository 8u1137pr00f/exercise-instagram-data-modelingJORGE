import os
import sys
from sqlalchemy import Column, ForeignKey, Enum, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey("user.id"), primary_key=True, nullable=False)
    user_to_id = Column(Integer, ForeignKey("user.id"), nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(250), unique=True, nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String, unique=True, nullable=False)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, nullable=False)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True, nullable=False)
    type = Column(Enum, nullable=False)
    url = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False)

    def to_dict(self):
        return {}

engine = create_engine('sqlite:///mydatabase.db')
Base.metadata.create_all(engine)

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=True)
    password = Column(String(50), nullable=True)
    created_at = Column(String(50))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('user.id'))
    created_at = Column(String(50))

class Post_comments(Base):
    __tablename__ = 'post_comments'
    id = Column(Integer, primary_key=True)
    postId = Column(Integer)
    userId = Column(Integer, ForeignKey('post.id'))
    created_at = Column(String(50))
    comment = Column(Integer)

class Post_likes(Base):
    __tablename__ = 'post_likes'
    id = Column(Integer, primary_key=True)
    postId = Column(Integer, ForeignKey('post.id'))
    userId = Column(Integer)
    created_at = Column(String(50))


class Photo(Base):
    __tablename__ = 'photo'
    id = Column(Integer, primary_key=True)
    postId = Column(Integer, ForeignKey('post.id'))
    userId = Column(Integer)
    url = Column(String(80))

class User_followers(Base):
    __tablename__ = 'user_followers'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('user.id'))
    followerId = Column(Integer)
    follow_at = Column(String(50))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

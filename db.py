from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

import os

Base = declarative_base()
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = 'sqlite:///' + os.path.join(basedir, './.videos.db')
engine = create_engine(db_path, echo=False)


class Video(Base):
    __tablename__ = 'video'
    id = Column(String, primary_key=True)


from db import engine, Video
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker, scoped_session

session = scoped_session(sessionmaker(bind=engine))

def in_db(vid):
    # search video in db by id
    if session.query(Video).filter(Video.id == vid).first():
        return True
    else:
        return False


def store_in_db(vid):
    new_video = Video(id=vid)
    session.add(new_video)
    session.commit()



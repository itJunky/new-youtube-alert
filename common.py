from db import engine, Video
import telebot
from conf import tgtoken, chat_id
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker, scoped_session

bot = telebot.TeleBot(tgtoken)
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


def send_to_tg(vid):
    url = 'https://www.youtube.com/watch?v={}'.format(vid)
    bot.send_message(chat_id, "Гринч сварганил новый видос \
            {}".format(url))


#!/usr/bin/env python3
# connect & use SQLite db

from sqlalchemy import create_engine

# echo flag sets up SQLAlchemy logging, shows all generated SQL produced
sql_engine = create_engine('sqlite:///:memory:', echo=True)

# declare mapping - create classes that  are defined in terms of a bas class
# maintain a catalog of classes & tables relative to that base
from sqlalchemy.ext.declarative import declarative_base

BaseClass = declarative_base()

from sqlalchemy import Column, Integer, String

# create user table to store records for end-users
class User(BaseClass):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fname = Column(String)
    nickname = Column(String)
    
    def __repr__(self):
        return f"<User(name='{self.name}', fullname='{self.fname}', nickname='{self.nickname}')>"

print()
print(User.__table__)
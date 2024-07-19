from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

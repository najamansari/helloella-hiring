from sqlalchemy import create_engine, Column, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Transformation(Base):
    __tablename__ = "transformation"
    input_hash = Column(String(256), primary_key=True)
    transformed = Column(Text)

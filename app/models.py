from sqlalchemy import create_engine, Column, String, Text
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


class Transformation(Base):
    __tablename__ = "transformation"
    input_hash = Column(String(256), primary_key=True)
    transformed = Column(Text)

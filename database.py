from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase
from config import config

url = config.DATABASE_URL
class Base(DeclarativeBase):
    pass

class MemoryEntry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    mem_type = Column(String)
    content = Column(String)

engine = create_engine(url)
Base.metadata.create_all(engine)
from sqlalchemy import create_engine, column, Integer, String, Date, Text
from sqlalchemy.orm import sessionmaker, declarative_base

Base=declarative_base()
engine=create_engine("sqlite:///events.db",echo=False)
SessionLocal = sessionmaker(bind=engine)

class Event(Base):
    __tablename__="events"
    id = column(Integer,primary_key=True, index=True)
    title= column(String, nullable=False)
    link=column(String,nullable=False)
    source=column(String,nullable=False)
    category=column(String,nullable=True)
    location=column(String,nullable=True)
    date=column(String,nullable=True)
    description=column(Text,nullable=True)
Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yeild db
    finally:
        db.close()
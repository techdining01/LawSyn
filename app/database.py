from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
import datetime

DATABASE_URL = "postgresql://postgres:idrees@localhost/lawsync" # Replace with your credentials

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Case(Base):
    __tablename__ = "cases"
    id = Column(Integer, primary_key=True, index=True)
    suit_no = Column(String, unique=True, index=True)
    state = Column(String)
    claimant = Column(String)
    defendant = Column(String)
    last_status = Column(String)
    lawyer_email = Column(String)
    last_synced = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(bind=engine)



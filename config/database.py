from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

URL_DATABASE = 'sqlite:///./messagesApp.db'

engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
        
def init_db():
    Base.metadata.create_all(engine)
    
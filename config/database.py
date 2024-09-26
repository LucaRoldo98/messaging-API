from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

URL_DATABASE = 'mysql+pymysql://root:rootroot@localhost:3306/MessageApplication'

engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        
def init_db():
    Base.metadata.create_all(engine)
    
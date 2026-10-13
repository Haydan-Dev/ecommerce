from sqlalchemy import create_engine # the imported variable is used for making low level connection to the MySQL 
from sqlalchemy.orm import sessionmaker,declarative_base  #ORM sttands for object relational mapper , and is used for maing python Classes into SQL Table

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/ecommerce"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
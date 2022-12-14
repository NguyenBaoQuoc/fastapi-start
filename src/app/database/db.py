from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost/my_test_db?charset=utf8"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()

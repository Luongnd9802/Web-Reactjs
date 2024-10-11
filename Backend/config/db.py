# from sqlalchemy import create_engine, MetaData

# engine = create_engine('mysql+pymysql://root:000000@localhost:3306/blogapplication')
# meta = MetaData()
# db = engine.connect()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:000000@mysql:3306/blogapplication"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 
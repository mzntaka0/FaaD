#from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

#from decouple import config


#SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{config('DB_USERNAME')}:{config('DB_PASSWORD')}@{config('DB_HOST')}/{config('DB_TABLE')}"
#engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#SQLALCHEMY_DATABASE_URI='sqlite:///./db.sqliste3'

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

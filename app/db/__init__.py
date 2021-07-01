#from decouple import config
#from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker
#
##SQLALCHEMY_DAsettings.TABASE_URL = "sqlite:///./sql_app.db"
#SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{config('DB_USERNAME')}:{config('DB_PASSWORD')}@{config('DB_HOST')}"
# print(SQLALCHEMY_DATABASE_URL)
##SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
#
# engine = create_engine(
#    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# print(vars(engine))
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
#Base = declarative_base()
# print(vars(Base))

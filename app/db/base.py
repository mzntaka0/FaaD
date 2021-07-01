# Import all the models, so that Base has them before being
# imported by Alembic
from decouple import config
from eralchemy import render_er

from app.db.base_class import Base  # noqa
from app.models import User, Blueprint, Coordinate, Field, Sensor  # noqa


#SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{config('DB_USERNAME')}:{config('DB_PASSWORD')}@{config('DB_HOST')}/{config('DB_TABLE')}"
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'

render_er(Base, 'app/public/erd_from_sqlalchemy.png')
render_er(SQLALCHEMY_DATABASE_URI, 'app/public/erd_from_rds.png')
render_er(Base, './erd.png')

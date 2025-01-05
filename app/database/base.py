
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

from app.files_navigation import join_absolute_path

SQLALCHEMY_DATABASE_URL = 'database/file/database.db'
SQLALCHEMY_DATABASE_URL = join_absolute_path(SQLALCHEMY_DATABASE_URL)
SQLALCHEMY_DATABASE_URL = f'''sqlite:///{SQLALCHEMY_DATABASE_URL}'''

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    '''Создание объекта сессии'''
    db = SessionLocal()
    return db

class Model(DeclarativeBase):
    metadata = MetaData(naming_convention={
     'ix': "'ix_%(column_0_label)s'", 
     'uq': "'uq_%(table_name)s_%(column_0_name)s'", 
     'ck': "'ck_%(table_name)s_`%(constraint_name)s`'", 
     'fk': "'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s'", 
     'pk': "'pk_%(table_name)s'"}
    )
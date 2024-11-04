from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = 'user'
DB_PASSWORD = 'postgress'
DB_HOST = 'localhost'  # Cambia esto si tu base de datos está en otro servidor
DB_PORT = '5432'       # Puerto por defecto de PostgreSQL
DB_NAME = 'base_test'

# Crea la URL de conexión
DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


engine = create_engine('sqlite:///aplicacion.sqlite')
Session = sessionmaker(bind=engine)

Base = declarative_base()
session = Session()
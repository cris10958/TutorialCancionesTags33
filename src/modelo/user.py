from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///aplicacion.sqlite')
Session = sessionmaker(bind=engine)

Base = declarative_base()
session = Session()

with engine.connect() as connection:
    connection.execute(text("CREATE TABLE users (id INTEGER PRIMARY KEY, username VARCHAR)"))
    connection.execute(text("INSERT INTO users (username) VALUES ('admin')"))

def get_user_by_username(username):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    with engine.connect() as connection:
        result = connection.execute(text(query))
        return result.fetchall()

user_input = "admin'; DROP TABLE users; --"
print(get_user_by_username(user_input))
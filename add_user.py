import email
from db import db_session

from models_ import User

user = User(name='Мария Сидорова', salary=150000, email='msidorova@yandex.ru')
db_session.add(user)
db_session.commit()
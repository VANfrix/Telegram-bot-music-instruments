import email
from db import db_session

from models_DB import User

user = User(name='Умар Махнов', salary=750000, email='Mah@yandex.ru')
db_session.add(user)
db_session.commit()
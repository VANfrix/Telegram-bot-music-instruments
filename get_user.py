from models_DB import User

user = User.query.first()
print(user)
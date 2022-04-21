from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
<<<<<<< HEAD
from sqlalchemy.orm import sessionmaker, scoped_session
from registration_db import reg_db_data

engine = create_engine(reg_db_data)
=======
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://sgveurqu:0MDVhW9jFUkyOBfYz_xt_8fgiqhXRPJc@hattie.db.elephantsql.com:5432/sgveurqu')
>>>>>>> 5e8e3ab0addb4d6feb03ad79037d04c064e602e3
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
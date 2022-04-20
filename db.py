from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://sgveurqu:0MDVhW9jFUkyOBfYz_xt_8fgiqhXRPJc@hattie.db.elephantsql.com:5432/sgveurqu')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
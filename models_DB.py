from sqlalchemy import Column, Integer, String
from db import Base, engine

class Guitar(Base):
    __tablename__ = 'guitars'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    available = Column(String)
    bonus = Column(Integer)
    link_guitar = Column(String)


    def __repr__(self):
        return f'Guitar id: {self.id}, name: {self.name}'



if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
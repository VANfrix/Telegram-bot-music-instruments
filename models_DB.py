from sqlalchemy import Column, Integer, String
from db import Base, engine

class Guitars(Base):
    __tablename__ = 'guitars'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    available = Column(String)
    bonus = Column(Integer)
    link_guitar = Column(String)


    def __repr__(self):
        return f'<User {self.name} {self.link_guitar}>'

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)


    # name_guitar = guitar.find('div', class_="title").text.strip()
    # price_guitar = guitar.find('p', class_="price").text.strip().replace(' ', '')
    # available_guitar = guitar.find('div', class_= "product-existence").text.strip()
    # bonus_guitar = guitar.find('span', class_= "product-add-bonus").text.strip()
    # link_guitar = guitar.find('div', class_='product-pictures').find_all('a')[1].get('href')
    # link_guitar = f"https://www.muztorg.ru/{link_guitar}"
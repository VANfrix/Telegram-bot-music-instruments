from db import db_session
from models_DB import Guitar
from utils import dict_list

guitar = Guitar(name= dict_list[name_guitar], price = dict_list[price], available = 'в наличии', bonus = '1000', link_guitar='https://loud-lemon.com/fender-avri-62-stratocaster-sonic-blue-usa-elektrogitara')
db_session.add(guitar)
db_session.commit()



# name_guitar = guitar.find('div', class_="title").text.strip()
# price_guitar = guitar.find('p', class_="price").text.strip().replace(' ', '')
# available_guitar = guitar.find('div', class_= "product-existence").text.strip()
# bonus_guitar = guitar.find('span', class_= "product-add-bonus").text.strip()
# picture_guitar = guitar.find('div', class_='product-pictures').find_all('a')[1].get('href')
# link_guitar = f"https://www.muztorg.ru/{link_guitar}"
import requests
from bs4 import BeautifulSoup

def get_html(url, search_string):
#     proxies = {
#   'http': 'http://188.170.233.109:3128',
# }
    HEADERS ={ "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","user-agent"
:"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
    try:
        result = requests.get(url, params = {'q': search_string}, headers=HEADERS)
        print(dir(result))
        print(result.url)
        # print(result.text)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError) as exec:
        print(exec)
        print("Сетевая ошибка")
        return False

def get_muztorg(search_string):
    html = get_html("https://www.muztorg.ru/category/elektrogitary", search_string)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_guitars = soup.find_all('section', class_='product-thumbnail')
        print(len(all_guitars))
        result_find = []
        for guitar in all_guitars:
            name_guitar = guitar.find('div', class_="title").text.strip()
            price_guitar = guitar.find('p', class_="price").getText().replace(' ', '')
            available_guitar = guitar.find('div', class_= "product-existence").text.strip()
            bonus_guitar = guitar.find('span', class_= "product-add-bonus").text.strip()
            
            result_find.append({
                "name_guitar": name_guitar,
                "price_guitar": price_guitar,
                "available_guitar": available_guitar,
                "bonus_guitar": bonus_guitar
            })
        # print(result_find)
        return result_find

if __name__ == "__main__":
    get_muztorg('электрогитара')
    
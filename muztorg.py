import requests
from bs4 import BeautifulSoup

def get_html(url, search_string, page):

    HEADERS ={ 
        "Accept": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
        }

    try:
        result = requests.get(url, params = {'q': search_string, 'in-stock': 1, 'page': page}, headers=HEADERS)
        print(result.url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError) as exec:
        print(exec)
        print("Сетевая ошибка")
        return False

def get_muztorg(search_string, page=0):
    html = get_html("https://www.muztorg.ru/category/elektrogitary", search_string, page)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_guitars = soup.find_all('section', class_='product-thumbnail')
        print(len(all_guitars))
        result_find = []
        for guitar in all_guitars:
            name_guitar = guitar.find('div', class_="title").text.strip()
            price_guitar = guitar.find('p', class_="price").text.strip().replace(' ', '')
            available_guitar = guitar.find('div', class_= "product-existence").text.strip()
            bonus_guitar = guitar.find('span', class_= "product-add-bonus").text.strip()
            link_guitar = guitar.find('div', class_='product-pictures').find_all('a')[1].get('href')
            link_guitar = f"https://www.muztorg.ru/{link_guitar}"
            
            result_find.append({
                "name_guitar": name_guitar,
                "price_guitar": price_guitar,
                "available_guitar": available_guitar,
                "bonus_guitar": bonus_guitar,
                "link_guitar": link_guitar
            })          
        return result_find
1
if __name__ == "__main__":
    get_muztorg('электрогитара')
    
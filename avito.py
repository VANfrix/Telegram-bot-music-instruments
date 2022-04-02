import requests
from bs4 import BeautifulSoup

def get_html(url, search_string):
    try:
        result = requests.get(url, params = {'q': search_string})
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False

def get_avito(search_string):
    html = get_html("https://www.avito.ru/moskva/muzykalnye_instrumenty?cd=1", search_string)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_guitars = soup.find_all('div', class_='iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum')
        print(len(all_guitars))
        result_find = []
        for guitar in all_guitars:
            name_guitar = guitar.find('h3', class_="title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL text-bold-SinUO").text
            price_guitar = guitar.find('span', class_="price-text-_YGDY text-text-LurtD text-size-s-BxGpL").text.replace('\xa0', '')
            name_saler = guitar.find('div', class_= "style-title-_wK5H text-text-LurtD text-size-s-BxGpL").text
            place_guitar = guitar.find('div', class_= "geo-georeferences-SEtee text-text-LurtD text-size-s-BxGpL").text.replace('\xa0', '')
            result_find.append({
                "name_guitar": name_guitar,
                "price_guitar": price_guitar,
                "name_saler": name_saler,
                "place_guitar": place_guitar
            })
        print(result_find)
        return result_find

if __name__ == "__main__":
    get_avito()
    
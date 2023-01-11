from muztorg import get_muztorg

def get_guitar_message(pages, search_string):
    page = pages//24+1
    guitars = get_muztorg(search_string, page)
    dict_list = ''
    while pages>24:
        pages=pages-24
    print(pages)

    for guitar in guitars[pages:pages+12]:
        name_=guitar['name_guitar']
        price_=guitar['price_guitar']
        available_=guitar['available_guitar']
        bonus_=guitar['bonus_guitar']
        link_=guitar['link_guitar']
        search_new = f'\t{name_}\n цена {price_}\n {available_}\n бонусы {bonus_}\n ссылка {link_}\n\n'
        dict_list += search_new
    return dict_list
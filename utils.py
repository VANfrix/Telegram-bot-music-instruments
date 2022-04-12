from muztorg import get_muztorg

def get_guitar_message(pages, search_string):
    guitars = get_muztorg(search_string)
    dict_list = ''
    for guitar in guitars[pages:pages+5]:
        name_=guitar['name_guitar']
        price_=guitar['price_guitar']
        available_=guitar['available_guitar']
        bonus_=guitar['bonus_guitar']
        search_new = f'\t{name_}\n цена {price_}\n {available_}\n бонусы {bonus_}\n\n'
        dict_list += search_new
        print(dict_list)
    return dict_list
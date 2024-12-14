def filter_by_state(dict_list: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа state,
    возвращает новый список словарей, содержащий только словари, у которых ключ
    state соответствует указанному значению"""
    newlist = []
    for slovar in dict_list:
        if slovar.get('state') == state:
            newlist.append(slovar)
    return newlist


def sort_by_date(dict_list: list[dict], order: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр, задающий
    порядок сортировки (по умолчанию — убывание). Функция должна возвращать
    новый список, отсортированный по дате (date)"""
    if order:
        return sorted(dict_list, key=lambda x: x['date'], reverse=True)
    else:
        return sorted(dict_list, key=lambda x: x['date'])

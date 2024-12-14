def filter_by_state(dict_list: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа state,
    возвращает новый список словарей, содержащий только словари, у которых ключ
    state соответствует указанному значению"""
    newlist = []
    for list_dictionary in dict_list:
        if list_dictionary.get('state') == state:
            newlist.append(list_dictionary)
    return newlist


def sort_by_date(dict_list: list[dict], order: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр, задающий
    порядок сортировки (по умолчанию — убывание). Функция должна возвращать
    новый список, отсортированный по дате (date)"""
    if order:
        return sorted(dict_list, key=lambda x: x['date'], reverse=True)
    else:
        return sorted(dict_list, key=lambda x: x['date'])

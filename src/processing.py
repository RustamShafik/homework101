def filter_by_state(dict_list: list[dict], state = 'EXECUTED') -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа state,
    возвращает новый список словарей, содержащий только словари, у которых ключ
    state соответствует указанному значению"""
    newlist = []
    for slovar in dict_list:
        if slovar.get('state') == state:
            newlist.append(slovar)
    return slovar


def sort_by_date(dict_list: list[dict]) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр, задающий
    порядок сортировки (по умолчанию — убывание). Функция должна возвращать
    новый список, отсортированный по дате (date)"""
    pass

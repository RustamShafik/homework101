import re
from collections import defaultdict

def transact_dict(transact_dictionary, searchstr):
    """
        Функция для поиска транзакций в списке по ключу 'description', используя строку поиска.
    """
    transact_list = []
    for transaction in transact_dictionary:
        # Преобразуем значение description в строку (чтобы избежать ошибок с NaN или float)
        description = str(transaction.get("description", ""))  # Преобразуем сразу в строку

        # Теперь проверка только по строке description
        if re.search(searchstr, description, re.IGNORECASE):  # Поиск по строке
            transact_list.append(transaction)
    return transact_list

def transact_count(transact_dictionary, category_list):
    """
        Функция для подсчёта количества транзакций по категориям.
    """
    category_count = defaultdict(int)
    for transaction in transact_dictionary:
        description = str(transaction.get("description", ""))

        if description in category_list:
            category_count[description] += 1
    return category_count



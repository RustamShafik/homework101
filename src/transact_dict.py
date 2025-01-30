import re
from collections import defaultdict

def transact_dict(transact_dictionary, searchstr):
    """
        Функция для поиска транзакций в списке по ключу 'description', используя строку поиска.
    """
    transact_list = []
    for transaction in transact_dictionary:
        if re.search(searchstr, transaction["description"], re.IGNORECASE):
            transact_list.append(transaction)
    return transact_list

def transact_count(transact_dictionary, category_list):
    """
        Функция для подсчёта количества транзакций по категориям.
    """
    category_count = defaultdict(int)
    for transaction in transact_dictionary:
        if transaction["description"] in category_list:
            category_count[transaction["description"]] += 1
    return category_count

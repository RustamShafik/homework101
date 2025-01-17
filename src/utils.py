import requests
import json

def transactions_dict_return(file_path):
    '''Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях'''
    trans_list = []
    try:
        with open(file_path) as file:
            try:
                trans_data = json.load(file)
                return trans_data
            except json.JSONDecodeError:
                return trans_list
    except FileNotFoundError:
        return trans_list

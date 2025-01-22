import json
import logging

logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('../logs/utils.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transactions_dict_return(file_path):
    '''Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях'''
    trans_list = []
    try:
        logger.debug(f'Запуск обработки файла по адресу {file_path}')
        with open(file_path, encoding='utf-8') as file:
            try:
                trans_data = json.load(file)
                return trans_data
            except json.JSONDecodeError:
                logger.error(f'Ошибка декодирования JSON в файле: {file_path}')
                return trans_list
    except FileNotFoundError:
        logger.error(f'Файл не найден: {file_path}')
        return trans_list


# if __name__ == "__main__":
#     transactions_dict_return("../data/operations.json")

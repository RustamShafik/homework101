from datetime import datetime
import json
import csv_xls_reader
import decorators
import external_api
import generators
import masks
import processing
import transact_dict
from utils import transactions_dict_return
import widget


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    transactions = []

    if choice == '1':
        file_path = input(f"Введите путь к JSON-файлу (по умолчанию ../data/operations.json): ")
        if not file_path:  # Если путь не был введен, используем путь по умолчанию
            file_path = "../data/operations.json"
        transactions = transactions_dict_return(file_path)

    elif choice == '2':
        file_path = input(f"Введите путь к CSV-файлу (по умолчанию ../transactions.csv): ")
        if not file_path:  # Если путь не был введен, используем путь по умолчанию
            file_path = "../transactions.csv"
        transactions = csv_xls_reader.read_transactions_csv(file_path)

    elif choice == '3':
        file_path = input(f"Введите путь к XLSX-файлу (по умолчанию ../transactions_excel.xlsx): ")
        if not file_path:  # Если путь не был введен, используем путь по умолчанию
            file_path = "../transactions_excel.xlsx"
        transactions = csv_xls_reader.read_transactions_xls(file_path)

    else:
        print("Некорректный выбор, попробуйте снова.")
        return

    if not transactions:
        print("Не удалось обработать файл или он пуст.")
        return

    # Запрос статуса
    valid_statuses = ("executed", "canceled", "pending")

    while True:
        status_choice = input("Введите статус, по которому необходимо выполнить фильтрацию.\n"
                              "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ").lower()
        print(f"Вы выбрали статус: {status_choice.upper()}")  # Отладочный вывод

        if status_choice in valid_statuses:
            print(f"Операции отфильтрованы по статусу \"{status_choice.upper()}\".")
            break  # Выход из цикла, если статус корректен
        else:
            print(f"Статус операции \"{status_choice}\" недоступен.\n"
                  "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                  "Доступные для фильтрования статусы: EXECUTED, CANCELED, PENDING")

    # Фильтрация транзакций по выбранному статусу
    transactions = [transaction for transaction in transactions if isinstance(transaction.get('state'), str) and transaction.get('state').lower() == status_choice]

    if not transactions:
        print(f"Нет транзакций с выбранным статусом \"{status_choice.upper()}\".")
        return

    # Приведение даты к datetime объектам
    for transaction in transactions:
        if 'date' in transaction and isinstance(transaction['date'], str):  # Проверяем наличие ключа 'date' и что это строка
            try:
                # Преобразуем строку в объект datetime
                transaction['date'] = datetime.fromisoformat(transaction['date'].replace("Z", "+00:00"))
            except ValueError:
                transaction['date'] = None  # Если не удалось преобразовать, ставим None
        else:
            transaction['date'] = None  # Если дата не строка или ее нет

    # Запрос сортировки по дате
    sort_by_date = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if sort_by_date == "да":
        order = input("Отсортировать по возрастанию (1) или по убыванию (2)? ").lower()
        if order == "1":
            # Сортировка: элементы с None (отсутствующие даты) окажутся в конце
            transactions = sorted(transactions, key=lambda x: (x.get('date') is not None, x.get('date')))
        elif order == "2":
            # Сортировка по убыванию: элементы с None окажутся в начале
            transactions = sorted(transactions, key=lambda x: (x.get('date') is not None, x.get('date')), reverse=True)
        else:
            print("Некорректный выбор, сортировка не выполнена.")

    # Преобразуем даты обратно в строки для JSON сериализации
    for transaction in transactions:
        if 'date' in transaction and isinstance(transaction['date'], datetime):
            transaction['date'] = transaction['date'].strftime("%Y-%m-%dT%H:%M:%S%z")  # Преобразуем дату в строку

    # Фильтрация по валюте
    show_rub_only = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if show_rub_only == "да":
        # transactions = [transaction for transaction in transactions if 'rub' in transaction.get('currency_code', '').lower()]
        transactions = [transaction for transaction in transactions
                        if ('rub' in transaction.get('currency_code', '').lower() or
                            ('operationAmount' in transaction and
                             'currency' in transaction['operationAmount'] and
                             transaction['operationAmount']['currency'].get('code', '').upper() == 'RUB'))]

    # Фильтрация по слову
    filter_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if filter_by_word == "да":
        filter_word = input("Введите слово для фильтрации: ")
        transactions = [transaction for transaction in transactions if filter_word in transaction.get('description', '').lower()]

    # Выводим результаты
    print("Распечатываю итоговый список транзакций...")
    print(json.dumps(transactions, indent=4, ensure_ascii=False))
    print(f"Всего банковских операций в выборке: {len(transactions)}")


if __name__ == '__main__':
    main()

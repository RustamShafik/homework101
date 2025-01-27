import csv

import pandas as pd


def read_transactions_csv(path):
    '''
    Читает CSV-файл с транзакциями и возвращает их в виде списка словарей.
    '''
    transactions = []
    with open(path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    print(transactions)
    return transactions


def read_transactions_xls(path):
    '''
    Читает Excel-файл с транзакциями и возвращает их в виде списка словарей.
    '''
    transactions = []
    excel_transactions = pd.read_excel(path)
    for index, row in excel_transactions.iterrows():
        dict = row.to_dict()
        transactions.append(dict)
    return transactions


if __name__ == '__main__':
    read_transactions_csv("../short.csv")

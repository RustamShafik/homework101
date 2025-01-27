import csv
import pandas as pd

def read_transactions_csv(path):
    transactions = []
    with open(path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    return transactions

def read_transactions_xls(path):
    transactions = []
    excel_transactions = pd.read_excel(path)
    for index, row in excel_transactions.iterrows():
        dict = row.to_dict()
        transactions.append(dict)
    return transactions
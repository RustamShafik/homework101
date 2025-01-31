import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

transaction = {
    "amount": 150.0,
    "currency": "EUR"
}


def convert_op(transaction):
    '''Функция принимает транзакцию в виде словаря {"amount": 150.0, "currency": "EUR"} и возвращает
    сумму транзакции в рублях'''
    trans_currency = transaction["currency"]
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={trans_currency}"

    headers = {
        "apikey": API_KEY
    }

    response = requests.request("GET", url, headers=headers)

    status_code = response.status_code
    if status_code != 200:
        return ("Произошла ошибка")
    result = response.json()
    return (transaction["amount"] * result["rates"]["RUB"])


if __name__ == '__main__':
    print(convert_op(transaction))
    print(type(convert_op(transaction)))

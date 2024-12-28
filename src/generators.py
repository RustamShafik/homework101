from typing import List, Dict, Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[Dict]:
    """Функция фильтрует транзакции по указанной валюте."""
    for item in transactions:
        if item["operationAmount"]["currency"]["name"] == currency:
            yield item

def transaction_descriptions (transactions: list[dict]) -> Iterator[str]:
    """Функция извлекает описание транзакций"""
    for item in transactions:
        yield item["description"]

def card_number_generator(start: int, finish: int) -> Iterator[str]:
    """Функция генерирует номера карт с разделением по 4 цифры"""
    for x in range(start, finish+1):
        formatted_number = f"{x:016d}"
        formatted_number_with_spaces = ' '.join([formatted_number[i:i + 4] for i in range(0, len(formatted_number), 4)])
        yield formatted_number_with_spaces
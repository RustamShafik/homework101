import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


@pytest.fixture
def sample_card_numbers():
    return [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]


def test_filter_by_currency(sample_transactions):
    usd_transactions = filter_by_currency(sample_transactions, "USD")
    result = list(usd_transactions)
    assert len(result) == 3
    for transaction in result:
        assert transaction["operationAmount"]["currency"]["name"] == "USD"


def test_transaction_descriptions(sample_transactions):
    result = list(transaction_descriptions(sample_transactions))
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert result == expected_descriptions


def test_card_number_generator(sample_card_numbers):
    result = list(card_number_generator(1, 3))
    assert result == sample_card_numbers


@pytest.mark.parametrize(
    "start, finish, expected",
    [(1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"])]
)
def test_card_number_generator_different_values(start, finish, expected):
    # Преобразуем генератор в список и сравниваем с ожидаемым результатом
    result = list(card_number_generator(start, finish))
    assert result == expected


@pytest.mark.parametrize(
    "currency, expected_count",
    [
        ("USD", 3),  # Ожидаем 3 транзакции с валютой USD
        ("руб.", 2),  # Ожидаем 2 транзакции с валютой руб.
        ("EUR", 0),  # Ожидаем, что не будет транзакций с валютой EUR
    ]
)
def test_filter_by_currency_with_parametrization(sample_transactions, currency, expected_count):
    filtered_transactions = filter_by_currency(sample_transactions, currency)
    result = list(filtered_transactions)
    assert len(result) == expected_count
    if expected_count > 0:
        for transaction in result:
            assert transaction["operationAmount"]["currency"]["name"] == currency


@pytest.mark.parametrize(
    "transactions, expected_descriptions",
    [
        (
            [
                {"description": "Перевод организации"},
                {"description": "Перевод со счета на счет"},
                {"description": "Перевод с карты на карту"},
            ],
            ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]
        ),
        (
            [
                {"description": "Оплата услуг"},
                {"description": "Перевод на карту"},
            ],
            ["Оплата услуг", "Перевод на карту"]
        ),
    ]
)
def test_transaction_descriptions_with_parametrization(transactions, expected_descriptions):
    result = list(transaction_descriptions(transactions))
    assert result == expected_descriptions

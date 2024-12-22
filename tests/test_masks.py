import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture()
def valid_card_numbers():
    return [
        ("7000794444446361", "7000 79** **** 6361"),
        ("7000794444446362", "7000 79** **** 6362"),
        ("7000794444446363", "7000 79** **** 6363"),
    ]


@pytest.fixture()
def valid_account_numbers():
    return [("73654108430135874305", "**4305"), ("73654108430135674375", "**4375"), ("73786896930135671111", "**1111")]


def test_get_account_number(valid_account_numbers):
    for account_numba, expected in valid_account_numbers:
        assert get_mask_account(account_numba) == expected


@pytest.mark.parametrize(
    "card_numba, expected",
    [
        ("7000794444446361", "7000 79** **** 6361"),
        ("7000794444446362", "7000 79** **** 6362"),
        ("7000794444446363", "7000 79** **** 6363"),
    ],
)
def test_get_mask_card_number(card_numba, expected):
    assert get_mask_card_number(card_numba) == expected


@pytest.mark.parametrize(
    "account, expected",
    [("73654108430135874305", "**4305"), ("73654108430135674375", "**4375"), ("73786896930135671111", "**1111")],
)
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected


def test_get_mask_card_incorrect_length():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("1")

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Номер карты должен содержать 16 символов"


def test_get_mask_account_not_string():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(156464564564564564564564568999999999)

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Номер счета должен представлять собой строку"


def test_get_mask_card_no_card_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(None)

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Отсутствует номер карты"


def test_get_mask_account_too_short():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("156")

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Номер счета должен содержать минимум 4 символа"

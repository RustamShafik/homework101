import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture()
def card_numbers():
    return ["7000 79** **** 6361", "7000 79** **** 6362", "7000 79** **** 6363"]

@pytest.mark.parametrize("card_numba, expected", [("7000794444446361", "7000 79** **** 6361"),
                                                  ("7000794444446362", "7000 79** **** 6362"),
                                                  ("7000794444446363", "7000 79** **** 6363")])
def test_get_mask_card_number(card_numba, expected):
    assert get_mask_card_number(card_numba) == expected

@pytest.mark.parametrize("account, expected", [("73654108430135874305", "**4305"),
                                                  ("73654108430135674375", "**4375"),
                                                  ("73786896930135671111", "**1111")])
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected





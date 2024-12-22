import pytest

from src.widget import get_date


@pytest.fixture
def mock_get_mask_account(monkeypatch):
    def mock(account):
        return "****" + account[-4:]

    monkeypatch.setattr("src.masks.get_mask_account", mock)


@pytest.fixture
def mock_get_mask_card_number(monkeypatch):
    def mock(card_number):
        return card_number[:4] + " **** **** " + card_number[-4:]

    monkeypatch.setattr("src.masks.get_mask_card_number", mock)


def test_get_date():
    date = "2024-03-11T02:26:18.671407"
    result = get_date(date)
    expected = "11.03.2024"
    assert result == expected


if __name__ == "__main__":
    pytest.main()
